import mahotas as mh
import cv2

import os
path = "data/Source/Stacks"
images = [f for f in os.listdir(path) if '.tif' in f.lower()]



for i in images:
    im = cv2.imread(path+"\\"+i)
    print(images[0])

# exporting the image and renaming
    img_output_path = "OUTPUT_FOLDER//"+i.replace("tif", "jpg")


    response = cv2.imwrite(img_output_path, im)

    if response:
       print("image stored at location: ", img_output_path)




"""
for i in images:
    im = Image.open(path+"\\"+i)
    print(images[0])

# JPG conversion
    rgb_im = im.convert("RGB")

# exporting the image and renaming
    rgb_im.save("OUTPUT_FOLDER//"+i.replace("tif", "jpg"))
    
    """


