from PIL import Image
from random import randint
import uuid
from multiprocessing import Pool
import os
def remove_clipart(filepath_filename):
    try:
        with Image.open(filepath_filename[0]) as im:
            x, y = im.size
            pixels = im.load()
            if im.mode == 'L' or type(pixels) == int or x < 200 or y < 200:
                os.rename(filepath_filename[0], '/home/ubuntu/storage/error_files/' + filepath_filename[1])
            else:   
                status = False

                for i in range(4):
                    light_pixel = 0

                    if i == 0:
                        x_pixel = 0
                        y_pixel = 0

                    if i == 1:
                        x_pixel = x - 35
                        y_pixel = 0

                    if i == 2:
                        x_pixel = 0
                        y_pixel = y - 1

                    if i == 3:
                        x_pixel = x - 35
                        y_pixel = y - 1

                    for k in range(30):
                        if len(pixels[x_pixel, y_pixel]) != 3:
                            status = True
                        else:
                            first = pixels[x_pixel, y_pixel][0]
                            second = pixels[x_pixel, y_pixel][1]
                            third = pixels[x_pixel, y_pixel][2]
                            if first > 246 and second > 246 and third > 246:
                                light_pixel += 1
                            x_pixel += 1
                    if light_pixel == 30:
                        status = True

                if status:
                    os.rename(filepath_filename[0], '/home/ubuntu/storage/BW_images/' + filepath_filename[1])
    except IOError:
        os.rename(filepath_filename[0], '/home/ubuntu/storage/error_files/' + filepath_filename[1])

if __name__ == "__main__":
    img_dir = r"./pixa_ready/"
    images = []

    for filename in os.listdir(img_dir):
        filepath = os.path.join(img_dir, filename)
        images.append([filepath, filename])

    pool = Pool(processes=16) 
    pool.map(remove_clipart, images)

    print("Done!")