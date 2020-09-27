from PIL import Image
import os, glob
import numpy as np
import random, math
import mydefines

# array of data image
X = []

# array of data label
Y = []

def add_sample (cat_idx, fname):
    img = Image.open(fname)
    img = img.convert('RGB')
    img = img.resize((img_width, img_height))
    data = np.asarray(img)
    X.append(data)
    Y.append(cat_idx)

def make_sample(files):
    global X, Y
    X = []
    Y = []
    for cat_idx, fname in files:
        add_sample(cat_idx, fname)
    return np.array(X), np.array(Y)

allfiles = []

for idx, cat in enumerate(categories):
    image_dir = root_dir + '/' + cat
    print (image_dir)
    files = glob.glob(image_dir + '/*.jpg')
    for f in files:
        allfiles.append((idx, f))

random.shuffle(allfiles)
X_train, Y_train = make_sample(allfiles)
np.savez(root_dir + training_data_dir + '/' + training_data_name, X_train, Y_train)