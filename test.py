from PIL import Image

import numpy as np
import matplotlib.pyplot as mpl

def load_image(file_path):
    try:
        img = Image.open(file_path)
        print(f"Image loaded successfully! Format: {img.format}, Size: {img.size}, Mode: {img.mode}")
        return img
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

def get_stuff_from_image(img):
    if img is None:
        print("No image to process.")
        return

    width, height = img.size
    pixel = np.matrix(np.ones((height, width)))
    print(f"Width: {width}, Height: {height}")

    for j in range(height):  # Rows
        for i in range(width):  # Columns
             pixel[j,i] = int(sum(img.getpixel((i, j))))
            #print(f"Pixel[{j}][{i}]: {pixel[j][i]}")
    print(f"Pixels: {pixel}")
    print("Image processing completed.")
    return np.matrix(pixel)

def make_matrix(something, img):
        if img is None:
            print("No image to process.")
            return

        width, height = img.size
        kernel = np.matrix([[0,2],[-2,1]])

        if width % 2 == 0: # dient der anschaulichkeit
            width = width
        elif width % 2 != 0:
            width = width - 1

        if height % 2 == 0:
            height = height
        elif height % 2 != 0:
            height = height - 1

        res = np.matrix(np.ones((int(height/2), int(width/2))))

        #############################################################
        ##           Hier muss der Kernel über something.          ##
        #############################################################

        print(f"res: {res}")
if __name__ == "__main__":
    image_path = "test_img_1.png"  # Path to image
    image = load_image(image_path)
    test = get_stuff_from_image(image)
    make_matrix(test, image)
