import os
from PIL import Image
from multiprocessing import Pool
def remove_small_files(path_name):
    try:
        with Image.open(path_name[0]) as im:
            x, y = im.size
            if x < 200 or y < 200:
                os.rename(path_name[0], '/home/ubuntu/storage/BW_images/' + path_name[1])
    except:
        print('Error!')
        os.rename(path_name[0], '/home/ubuntu/storage/error_files/' + path_name[1])

if __name__ == "__main__":
    img_dir = r"./pixa_ready/"
    images = []

    for filename in os.listdir(img_dir):
        filepath = os.path.join(img_dir, filename)
        images.append([filepath, filename])

    pool = Pool(processes=16) 
    pool.map(remove_small_files, images)

    print("Done!")