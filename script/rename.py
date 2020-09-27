import glob
import os

path = 'C:/Users/PaPa/Documents/PyProjects/deepleaning/training/photo/skeleton'
files = glob.glob(path + '/*')

index = 0
for f in files:
    os.rename (f, os.path.join(path, 'skeleton_img' + str(index) + '.jpg'))
    index +=1