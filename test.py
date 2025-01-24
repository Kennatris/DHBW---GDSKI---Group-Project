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

    # Kernel, der horizontale Kanten hervorhebt
    kernel = np.array([[-3, -3, -3],
                       [6, 6, 6],
                       [-3, -3, -3]])

    result = convolve2d(pixel_matrix, kernel, mode='valid')

    print(f"Convolved Matrix: \n{result}")

    # Normierung der Werte auf 0-255 für Bilddarstellung
    result_normalized = (result - result.min()) / (result.max() - result.min()) * 255

    return result_normalized


def max_pooling(matrix, pool_size=2, stride=2):
    """
    Max-Pooling-Operation auf die Eingabematrix anwenden.
    :param matrix: Eingabematrix (Feature-Map)
    :param pool_size: Größe des Pooling-Fensters (z.B. 2x2)
    :param stride: Schrittweite des Poolings (meistens 2)
    :return: Poolierte Matrix
    """

    # Berechne die Größe der gepoolten Matrix
    pooled_height = (matrix.shape[0] - pool_size) // stride + 1
    pooled_width = (matrix.shape[1] - pool_size) // stride + 1
    pooled_matrix = np.zeros((pooled_height, pooled_width))

    # Max-Pooling durchführen
    for i in range(pooled_height):
        for j in range(pooled_width):
            # Finde den Bereich des Pooling-Fensters
            start_i = i * stride
            start_j = j * stride
            window = matrix[start_i:start_i + pool_size, start_j:start_j + pool_size]
            # Finde das Maximum im Fenster
            pooled_matrix[i, j] = np.max(window)

    return pooled_matrix


def create_image(norm_conv_matrix, name):
    result_image = Image.fromarray(norm_conv_matrix.astype(np.uint8))

    # Bild anzeigen
    plt.imshow(result_image, cmap="gray")
    plt.title(name)
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    image_path = "test_img_1.png"  # Path to image
    image = load_image(image_path)
    pixel_m = get_stuff_from_image(image)
    norm_conv_matrix = make_matrix(pixel_m, image)
    create_image(norm_conv_matrix, "Convolved Image")
    pooled_matrix = max_pooling(norm_conv_matrix, 2, 2)
    create_image(pooled_matrix, "Pooled Image")
