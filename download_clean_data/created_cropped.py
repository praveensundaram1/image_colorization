from PIL import Image
from random import randint
import uuid
from multiprocessing import Pool
import os
img_dir = r"./all_images/"
k = 0

def crop_images(path_and_file):
    try:
        with Image.open(path_and_file[0]) as im:
            x, y = im.size
            crop_quantity = int((x*y) / (224*224))

            for i in range(crop_quantity):
                first_x = randint(0, (x-230))
                first_y = randint(0, (y-230))
                second_x = randint(first_x + 224, x)
                second_y = randint(first_y + 224, y)
                box = (first_x, first_y, second_x, second_y)
                cropped_image = im.crop(box)
                cropped_image.save('/home/ubuntu/storage/cropped_images/' + str(uuid.uuid4()) + '.jpg')
    except IOError:
        os.rename(path_and_file[0], '/home/ubuntu/storage/error_files/' + path_and_file[1])

if __name__ == "__main__":
    img_dir = r"./all_images/"
    images = []

    for filename in os.listdir(img_dir):
        filepath = os.path.join(img_dir, filename)
        images.append([filepath, filename])

    pool = Pool(processes=16) 
    pool.map(crop_images, images)

    print("Done!")