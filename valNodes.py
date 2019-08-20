import numpy as np
import mrcfile as mrc
import pandas as pd
from scipy.spatial import distance
import heapq
import matplotlib.pyplot as plt
import os.path


dir_main = '/dls/ebic/data/staff-scratch/Donovan/testdata/BetaGal_CarbonEdge/cryolo_finetune/'
comparison = '/dls/ebic/data/staff-scratch/Donovan/testdata/BetaGal_CarbonEdge/cryolo_finetune/train_annotation/FoilHole_27272864_Data_27266981_27266982_20180428_0909-168420.box'

global TotFP
TotFP = 0
global TotFN
TotFN = 0
global TotTP
TotTP = 0

def files(no_ext, dir_main):
    im_file = dir_main+'train_image/'+no_ext+'.mrc'
    box_file = dir_main+'boxfiles/EMAN/'+no_ext+'.box'
    with mrc.open(im_file, permissive=True) as f:
        image = f.data
    return image, box_file


def plotter(image, box_coord, comp_coord):
    plt.imshow(image)
    x_coord_comp = comp_coord[:,0]
    y_coord_comp = comp_coord[:,1]
    plt.plot(x_coord_comp, y_coord_comp, 'o', color = 'green', alpha = 0.4)
    x_coord = box_coord[:,0]
    y_coord = box_coord[:,1]
    plt.plot(x_coord, y_coord, 'o', color = 'red', alpha = 0.4)
    plt.show()

def second_largest(numbers):
    sort_ind = numbers.argsort()
    closest_distances = numbers[sort_ind[0:2]]
    return sort_ind[0:2], closest_distances, sort_ind[0:2]


def closest_node(node, nodes):
    node_index = distance.cdist([node], nodes)[0]
    closest_index = second_largest(node_index)[0]
    closest_distance = second_largest(node_index)[1]
    net_points = second_largest(node_index)[2]
    close_dist_id = dict(zip(closest_distance, net_points))
    return close_dist_id


def close_enough(dist, limit = 60):
    close_points = []
    for i in dist:
        if i < limit:
            close_points.append(dist[i])
    return  close_points

def prep(box_file):
    boxes = pd.read_csv(box_file, sep='\t', header = None)
    box_val = boxes.values
    box_coord = box_val[:,0:2]
    return box_coord

def calcs(box_coord, comp_coord):
    FP = 0
    TP = 0
    for i in range(box_coord.shape[0]):
            point = box_coord[i,:]
            close_dist_id = closest_node(point, comp_coord)
            same_point = np.array(close_enough(close_dist_id))
            if same_point.shape[0] == 0:
                print("No shared point")
                FP += 1
            elif same_point.shape[0] == 1:
                print(f"Point {point} is the same as {comp_coord[same_point]}")
                TP += 1  
            else:
                print("Error: Too many close points")
    print(f"Number of false postives: {FP}")
    FN = comp_coord.shape[0] - TP
    print(f"Number of false negatives: {FN}")
    print(f"Number of true positives : {TP}")
    global TotFP
    global TotFN
    global TotTP
    TotFP += FP
    TotFN += FN
    TotTP += TP
    



ims = os.listdir(dir_main+'train_annotation')
# MAIN
for x in ims:
        print(x)
        infile = x
        no_ext = os.path.splitext(infile)[0]
        image = files(no_ext, dir_main)[0]
        box_file = files(no_ext, dir_main)[1]
        comp_file = dir_main +  'train_annotation/' + no_ext + '.box'
        box_coord = prep(box_file)
        comp_coord = prep(comp_file)
        calcs(box_coord, comp_coord)
        plotter(image, box_coord, comp_coord)
        #plt.savefig('./masks/{}.png'.format(no_ext))

print(f"Total number of false postives: {TotFP}")
print(f"Total number of false negatives: {TotFN}")
print(f"Total number of true positives : {TotTP}")
