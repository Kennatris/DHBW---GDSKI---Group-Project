import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from scipy.signal import convolve2d


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

    img_array = np.asarray(img.convert("L"))  # Graustufenbild für einfachere Verarbeitung
    print(f"Processed Image Shape: {img_array.shape}")
    return img_array


def make_matrix(pixel_matrix, img):
    if img is None or pixel_matrix is None:
        print("No image to process.")
        return None

    kernel = np.array([[0, 2], [-2, 1]])  # Beispielkernel
    result = convolve2d(pixel_matrix, kernel, mode='valid')

    print(f"Convolved Matrix: \n{result}")

    # Normierung der Werte auf 0-255 für Bilddarstellung
    result_normalized = (result - result.min()) / (result.max() - result.min()) * 255

    return result_normalized


def create_image(norm_conv_matrix):
    result_image = Image.fromarray(norm_conv_matrix.astype(np.uint8))

    # Bild anzeigen
    plt.imshow(result_image, cmap="gray")
    plt.title("Convolved Image")
    plt.axis("off")
    plt.show()

    # Bild speichern
    result_image.save("convolved_image.png")
    print("Convolved image saved as 'convolved_image.png'")


if __name__ == "__main__":
    image_path = "test_img_1.png"  # Path to image
    image = load_image(image_path)
    pixel_m = get_stuff_from_image(image)
    norm_conv_matrix = make_matrix(pixel_m, image)
    create_image(norm_conv_matrix)
