import os
from PIL import Image
from shutil import copyfile
img_dir = r"./all_images/"

images = []
for filename in os.listdir(img_dir):
    images.append(filename)

images.sort()

def get_orgname(org_name):
    name = org_name.partition(" ")[0]
    if name == org_name:
        name = org_name.partition(".")[0]
    return name

def get_size(filepath):
    with Image.open(first_filepath) as im:
        x, y = im.size
    return x * y
    

curr_name = ''
for i in range(len(images) - 1):
    if curr_name == '':
        curr_name = images[i]
        
    second_name = images[i + 1]
    
    if get_orgname(curr_name) == get_orgname(second_name):
        first_filepath = os.path.join(img_dir, curr_name)
        second_filepath = os.path.join(img_dir, second_name)
        first_size = get_size(first_filepath)
        second_size = get_size(second_filepath)
        
        if first_size < second_size:
            curr_name = second_name
        i += 1
    else:
        copyfile(os.path.join(img_dir, curr_name), '/home/ubuntu/storage/org_large/' + curr_name)
        curr_name = ''
        i += 1