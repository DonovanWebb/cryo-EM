import numpy as np
import mrcfile as mrc
import pandas as pd
from scipy.spatial import distance
import heapq
import matplotlib.pyplot as plt


infile = '/dls/ebic/data/staff-scratch/Donovan/testdata/Ap_K2_PP_GO/cryolo_impurities/box_files_with_flip/EMAN/FoilHole_22247924_Data_22246559_22246561_20180623_1736-193306.box'
imfile = '/dls/ebic/data/staff-scratch/Donovan/testdata/Ap_K2_PP_GO/cryolo_impurities/full_data/FoilHole_22247924_Data_22246559_22246561_20180623_1736-193306.mrc'

def files(imfile):
    with mrc.open(imfile, permissive=True) as f:
	image = f.data
    return image


def plotter(image, box_coord):
    plt.imshow(image)
    x_coord = box_coord[:,0]
    y_coord = box_coord[:,1]
    plt.plot(x_coord, y_coord, 'o', color = 'red')
    plt.show()

def second_largest(numbers):
    sort_ind = numbers.argsort()
    closest_distances = numbers[sort_ind[1:9]]
    return sort_ind[1], closest_distances, sort_ind[1:9]


def closest_node(node, nodes):
    node_index = distance.cdist([node], nodes)[0]
    closest_index = second_largest(node_index)[0]
    closest_distance = second_largest(node_index)[1]
    net_points = second_largest(node_index)[2]
    close_dist_id = dict(zip(closest_distance, net_points))
    close_enough(close_dist_id)
    return nodes[closest_index, :]


def close_enough(dist, limit = 150):
    net_count = 0
    close_points = []
    for i in dist:
        if i < limit:
            net_count += 1
            close_points.append(dist[i])
    print(close_points)
    return  close_points

def net_maker(box_coord):
    ids = np.array(range(0,len(box_coord)))
    dictionary = dict(zip(ids, box_coord))
    for i in dictionary:
        print(i)


# MAIN
boxes = pd.read_csv(infile, sep='\t', header = None)
box_val = boxes.values
box_coord = box_val[:,0:2]


for i in range(box_coord.shape[0]):
    point = box_coord[i,:]
    print("Init point: ", point)
    print("Closest point: ", closest_node(point, box_coord))

image = files(imfile)
plotter(image, box_coord)

net_maker(box_coord)
