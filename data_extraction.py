import mrcfile as mrc
#import exheader.py as head
import matplotlib.pyplot as plt
import numpy as np

infile = '/dls/ebic/data/staff-scratch/Yuriy/DataFileTypes/m02K2EPU_Mrc/em16619-23/GridSquare_9897066/FoilHole_9907179_Data_9923659_9923661_20190711_122055.mrc' # K2 Non-linear
#infile = '/dls/ebic/data/staff-scratch/Yuriy/DataFileTypes/m06K3EPU_Mrc/em20287-23/FoilHole_7821234_Data_7825668_7825670_20190708_1608.mrc' # k3 Non-linear
#infile = '/dls/ebic/data/staff-scratch/Yuriy/DataFileTypes/m02K2EPU_Mrc/em16619-23/GridSquare_9897066/FoilHole_9907179_Data_9923659_9923661_20190711_122055-376198_frames.mrc' # K2 Non-linear frames
#infile = '/dls/ebic/data/staff-scratch/Yuriy/DataFileTypes/m06K3EPU_Mrc/em20287-23/FoilHole_7821234_Data_7825668_7825670_20190708_1608_fractions.mrc' # K3 Super resolution

with mrc.open(infile) as f:
	data = np.array(f.data)
	print(data.shape)
	max_val = np.max(data)
	min_val = np.min(data)
	print(min_val)
	print(max_val)
	x = data.shape[1]
	y = data.shape[0]
	transform = np.zeros((y,x))
for x in range(len(data)):
	for y in range(len(data[x])):
		if data[x][y] < 5000:
			transform[x][y] = 0
		else:
			transform[x][y] = (data[x][y] - min_val)*256/(max_val-min_val)
plt.imshow(transform, cmap='gray')
plt.show()
print transform
print data
file = open('data.txt', 'w')
np.savetxt(file,data)
file.close()
	
