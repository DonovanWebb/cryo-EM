import mrcfile as mrc
import matplotlib.pyplot as plt
import pandas as pd

box_file = pd.read_csv('/dls/ebic/data/staff-scratch/Donovan/cryolo_tests/beta_gal/boxfiles/EMAN/20170629_00021_frameImage.box', sep='\s+', names=['A', 'B', 'C', 'D'])
im_file = '/dls/ebic/data/staff-scratch/Donovan/cryolo_tests/beta_gal/full_data/20170629_00021_frameImage.mrc'

with mrc.open(im_file, permissive = True) as f:
    data = f.data


plt.imshow(data,cmap = 'gray', origin = 'lower')

for x,y in zip(box_file['A'],box_file['B']):
	plt.scatter(x+256/2,y+256/2,marker = 's', color = 'r', s = 256)

plt.show()
