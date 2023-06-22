import os
import random
from PIL import Image

"""
取子集进行处理
"""
output_dir = './dataset/images_ILSVRC2012/val_sub/'

path = './dataset/imagenet/val/'
folders = os.listdir(path)
for i in range(1, len(folders) + 1):
    img_names = os.listdir(path + folders[i - 1])
    idx = random.randint(0, 49)
    img_name = path + folders[i - 1] + '/' + img_names[idx]
    img = Image.open(img_name).convert('RGB')
    output = img.resize((299, 299), resample=Image.ANTIALIAS)
    output_name = output_dir + ('%d.png' % i)
    output.save(output_name)

"""
整个数据集处理
"""
output_dir = './dataset/images_ILSVRC2012/val/'
path = './dataset/imagenet/val/'
folders = os.listdir(path)
for folder in folders:
    img_names = os.listdir(path + folder)
    for img_name in img_names:
        img = Image.open(path + folder + '/' + img_name).convert('RGB')
        output = img.resize((299, 299), resample=Image.ANTIALIAS)
        img_name = img_name.split('.')[0]
        output_name = output_dir + (img_name + '.png')
        output.save(output_name)
