from shutil import copyfile
import os
img_dir = r"./clipart_new/"

k = 0
s = 0
for filename in os.listdir(img_dir):
    
    if s < 100:
        filepath = os.path.join(img_dir, filename)
        copyfile(filepath, '/home/ubuntu/storage/clipart/' + filename)
        s += 1
    k += 1