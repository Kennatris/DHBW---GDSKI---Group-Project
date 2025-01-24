from PIL import Image
import numpy as np
import matplotlib.pyplot as mpl

kernel = np.array([[0, 2], [-2, 1]])

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
    pixel = np.ones((height, width))
    print(f"Width: {width}, Height: {height}")

    for j in range(height):  # Rows
        for i in range(width):  # Columns
            tmp = img.getpixel((i, j))[0] + img.getpixel((i, j))[1] + img.getpixel((i, j))[2]
            if tmp >= 255:
                pixel[j, i] = 0
            else:
                pixel[j, i] = 255

    print(f"Pixels: {pixel}")
    print("Image processing completed.")
    return pixel

def make_matrix(pixel_matrix, img):
    if img is None:
        print("No image to process.")
        return

    width, height = img.size

    if width % 2 == 0:  # dient der anschaulichkeit
        width = width
    elif width % 2 != 0:
        width = width - 1

    if height % 2 == 0:  # dient der anschaulichkeit
        height = height
    elif height % 2 != 0:
        height = height - 1

    res = np.ones((height // 2, width // 2))

    #############################################################
    ##           Hier muss der Kernel über die Matrix.         ##
    #############################################################

    for j in range(0, height - 1, 2):
        for i in range(0, width - 1, 2):
            region = pixel_matrix[j:j+2, i:i+2]
            if region.shape == (2, 2):
                rotated_kernel = np.rot90(kernel, 2)  # Rotate kernel by 180 degrees
                res[j // 2, i // 2] = np.sum(region * rotated_kernel)

    return res

def max_matrix(value):
    if value is None:
        return None

    kernel_size = kernel.shape
    output_height = value.shape[0] - kernel_size[0] + 1
    output_width = value.shape[1] - kernel_size[1] + 1
    max_res = np.zeros((output_height, output_width))

    for j in range(output_height):
        for i in range(output_width):
            region = value[j:j+kernel_size[0], i:i+kernel_size[1]]
            max_res[j, i] = np.max(region)

    print("Max matrix computed.")
    return max_res

if __name__ == "__main__":
    image_path = "0.png"  # Path to image
    image = load_image(image_path)
    pixel_m = get_stuff_from_image(image)

    goal = make_matrix(pixel_m, image)

    # Plotet das Bild #
    mpl.imshow(goal, cmap='gray')
    mpl.title('Image 0')
    mpl.axis('off')
    mpl.show()
    ##################

    goal = max_matrix(goal)

    # Plotet das Bild #
    mpl.imshow(goal, cmap='gray')
    mpl.title('Image 0')
    mpl.axis('off')
    mpl.show()
    ##################
