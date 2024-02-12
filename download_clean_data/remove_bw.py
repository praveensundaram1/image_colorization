from PIL import Image
from random import randint
import uuid
from multiprocessing import Pool
import os
def remove_bw(filepath_filename):
    try:
        with Image.open(filepath_filename[0]) as im:
            x, y = im.size
            pixels = im.load()
            if im.mode == 'L' or type(pixels) == int:
                os.rename(filepath_filename[0], '/home/ubuntu/storage/BW_images/' + filepath_filename[1])
            else:
                bw_pixel = 0
                for i in range(1000):
                    x_pixel = randint(0, (x-1))
                    y_pixel = randint(0, (y-1))
                    if len(pixels[x_pixel, y_pixel]) != 3:
                        bw_pixel += 1000
                    else:
                        match_pixel = pixels[x_pixel, y_pixel][0]
                        if match_pixel == pixels[x_pixel, y_pixel][1] or match_pixel == pixels[x_pixel, y_pixel][2]:
                            bw_pixel += 1
                if bw_pixel > 990:
                    os.rename(filepath_filename[0], '/home/ubuntu/storage/BW_images/' + filepath_filename[1])
    except:
        print('Error!')
        os.rename(filepath_filename[0], '/home/ubuntu/storage/error_files/' + filepath_filename[1])

if __name__ == "__main__":
    img_dir = r"./pixa_ready/"
    images = []

    for filename in os.listdir(img_dir):
        filepath = os.path.join(img_dir, filename)
        images.append([filepath, filename])

    pool = Pool(processes=16) 
    pool.map(remove_bw, images)

    print("Done!")