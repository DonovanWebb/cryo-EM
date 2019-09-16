# Options file for relion_it.py

### General parameters
# Pixel size in Angstroms in the input movies
angpix = 0.885
# Acceleration voltage (in kV)
voltage = 300.0
# Polara = 2.0; Talos/Krios = 2.7; some Cryo-ARM = 1.4
Cs = 2.7


### Import images (Linux wild card; movies as *.mrc, *.mrcs, *.tiff or *.tif; single-frame micrographs as *.mrc)
import_images = 'Movies/*.tif'
# Are these multi-frame movies? Set to False for single-frame micrographs (and motion-correction will be skipped)
images_are_movies = True


### MotionCorrection parameters
# Dose in electrons per squared Angstrom per frame
motioncor_doseperframe = 1.0
# Gain-reference image in MRC format (only necessary if input movies are not yet gain-corrected, e.g. compressed TIFFs from K2)
motioncor_gainreference = 'Movies/gain.mrc'


stop_after_ctf_estimation = True
