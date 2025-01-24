# Um die Bilder zu laden
from PIL import Image

# Für die Mathematik
import numpy as np

# Für die Bilder
import matplotlib.pyplot as mpl


# Lädt das Bild in Python rein
def load_image(file_path):
    try:
        img = Image.open(file_path)  # Bild wird geöffnet
        print(f"Bild erfolgreich geladen! Format: {img.format}, Größe: {img.size}, Modus: {img.mode}")
        return img
    except Exception as e:
        print(f"Fehler beim Laden des Bildes: {e}")
        return None


# liest die RGB Werte von den Bildern aus, und konvertiert diese in einen Array, welche nur aus 0 oder 255 besteht
def get_stuff_from_image(img):
    if img is None:
        print("Kein Bild zum Verarbeiten verfügbar.")
        return None

    width, height = img.size  # Bildbreite und -höhe
    pixel = np.ones((height, width))  # Initialisiere eines Arrays
    print(f"Breite: {width}, Höhe: {height}")

    # Iterieret über alle Pixel des Bildes
    for j in range(height):  # Zeilen
        for i in range(width):  # Spalten
            tmp = img.getpixel((i, j))[0] + img.getpixel((i, j))[1] + img.getpixel((i, j))[2]  # Summiert alle RGB-Werte und lässt den Transparents-Wert wegfallen
            if tmp >= 255:
                pixel[j, i] = 0  # Weißer Pixel (wird als (255, 255, 255, t) ausgelesen)
            else:
                pixel[j, i] = 255  # Schwarzer Pixel (wird als (0, 0, 0, t) ausgelesen)

    print("Bildverarbeitung abgeschlossen.")
    return pixel


# lässt den Kernel über die Matrix (Array) laufen und
def make_matrix(pixel_matrix, img, kernel):
    if img is None or pixel_matrix is None:
        print("Kein Bild zum Verarbeiten verfügbar.")
        return None

    width, height = img.size
    kernel_height, kernel_width = kernel.shape  # Größe des Kernels

    # Überprüfung das keine Polstellen entstehen
    if width % kernel_width != 0:
        width -= width % kernel_width
    if height % kernel_height != 0:
        height -= height % kernel_height

    res = np.ones((height // kernel_height, width // kernel_width))  # Ergebnis Matrix (Array)

    # Iteriere über die Matrix (Array) mit dem Kernel
    for j in range(0, height - kernel_height + 1, kernel_height):
        for i in range(0, width - kernel_width + 1, kernel_width):
            region = pixel_matrix[j:j + kernel_height, i:i + kernel_width]  # nimmt einen Ausschnitt der Matrix
            if region.shape == (kernel_height, kernel_width):
                rotated_kernel = np.rot90(kernel, 2)  # Kernel um 180° drehen
                res[j // kernel_height, i // kernel_width] = np.sum(region * rotated_kernel)  # convolution

    return res


# Funktion zur Berechnung der Maximalwerte in einer Matrix basierend auf einem Kernel
def max_matrix(value, kernel):
    if value is None:
        return None

    kernel_height, kernel_width = kernel.shape  # Größe des Kernels
    output_height = value.shape[0] - kernel_height + 1
    output_width = value.shape[1] - kernel_width + 1
    max_res = np.zeros((output_height, output_width))  # Ergebnis-Matrix

    # Iteriere über die Matrix und finde Maximalwerte
    for j in range(output_height):
        for i in range(output_width):
            region = value[j:j + kernel_height, i:i + kernel_width]  # Ausschnitt der Matrix
            max_res[j, i] = np.max(region)  # Maximalwert berechnen

    print("Maximalwert-Matrix berechnet.")
    return max_res


# Plottet ein Bild
def plot_image(matrix, title):
    # mpl.imshow(matrix, cmap='BrBG')  # Darstellung mit Farben
    mpl.imshow(matrix, cmap='Greys')  # Darstellung in Graustufen
    mpl.suptitle(title)  # Titel setzen
    mpl.axis('on')  # Achsen einblenden
    mpl.show()


if __name__ == "__main__":
    image_path = "0.png"  # Pfad zum Bild
    image = load_image(image_path)  # Bild laden
    pixel_m = get_stuff_from_image(image)  # Bild in Binärmatrix umwandeln

    plot_image(pixel_m.copy(), f"Pixel Matrix {image_path}")

    # kernel = np.array([[-1, 2, -1],[-1, 2, -1],[-1, 2, -1]])  # Kernel vertikal
    # kernel = np.array([[2, 2, 2],[-4, -4, -4],[2, 2, 2]])  # Kernel horizontal
    kernel = np.array([[1, 2, 1],[1, 2, 1],[1, 2, 1]])  # sharpening


    layer_count = 2  # Anzahl der Layer
    current_matrix = pixel_m

    # Iterative Verarbeitung und Darstellung der Ergebnisse
    for iteration in range(layer_count):
        print(f"Iteration {iteration + 1}: Anwenden von make_matrix.")
        current_matrix = make_matrix(current_matrix, image, kernel)  # Faltung mit Kernel
        plot_image(current_matrix, f"Iteration {iteration + 1} - Nach make_matrix")

        print(f"Iteration {iteration + 1}: Anwenden von max_matrix.")
        current_matrix = max_matrix(current_matrix, kernel)  # Maximalwert-Matrix berechnen
        plot_image(current_matrix, f"Iteration {iteration + 1} - Nach max_matrix")

    print("Verarbeitung abgeschlossen.")
