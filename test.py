from PIL import Image
import numpy as np
import matplotlib.pyplot as mpl


# Funktion zum Laden eines Bildes aus einer Datei
def load_image(file_path):
    try:
        img = Image.open(file_path)  # Bild wird geöffnet
        print(f"Bild erfolgreich geladen! Format: {img.format}, Größe: {img.size}, Modus: {img.mode}")
        return img
    except Exception as e:
        print(f"Fehler beim Laden des Bildes: {e}")
        return None


# Funktion zur Verarbeitung der Bildpixel und Konvertierung in eine Binärmatrix
def get_stuff_from_image(img):
    if img is None:
        print("Kein Bild zum Verarbeiten verfügbar.")
        return None

    width, height = img.size  # Bildbreite und -höhe werden abgerufen
    pixel = np.ones((height, width))  # Initialisiere eine Matrix mit Einsen
    print(f"Breite: {width}, Höhe: {height}")

    # Iteriere über alle Pixel des Bildes
    for j in range(height):  # Zeilen
        for i in range(width):  # Spalten
            tmp = img.getpixel((i, j))[0] + img.getpixel((i, j))[1] + img.getpixel((i, j))[2]  # Summiere RGB-Werte
            if tmp >= 255:
                pixel[j, i] = 0  # Schwarzer Pixel
            else:
                pixel[j, i] = 255  # Weißer Pixel

    print("Bildverarbeitung abgeschlossen.")
    return pixel


# Funktion zur Reduktion der Matrixgröße basierend auf einem Kernel
def make_matrix(pixel_matrix, img, kernel):
    if img is None or pixel_matrix is None:
        print("Kein Bild zum Verarbeiten verfügbar.")
        return None

    width, height = img.size
    kernel_height, kernel_width = kernel.shape  # Größe des Kernels

    # Passen Sie die Breite und Höhe an, um ganzzahlige Schritte zu gewährleisten
    if width % kernel_width != 0:
        width -= width % kernel_width
    if height % kernel_height != 0:
        height -= height % kernel_height

    res = np.ones((height // kernel_height, width // kernel_width))  # Ergebnis-Matrix

    # Iteriere über das Bild mit dem Kernel
    for j in range(0, height - kernel_height + 1, kernel_height):
        for i in range(0, width - kernel_width + 1, kernel_width):
            region = pixel_matrix[j:j + kernel_height, i:i + kernel_width]  # Ausschnitt der Matrix
            if region.shape == (kernel_height, kernel_width):
                rotated_kernel = np.rot90(kernel, 2)  # Kernel um 180° drehen
                res[j // kernel_height, i // kernel_width] = np.sum(region * rotated_kernel)  # Faltung

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


# Funktion zur dynamischen Darstellung einer Matrix als Bild
def plot_image(matrix, title):
    mpl.imshow(matrix, cmap='BrBG')  # Darstellung in Graustufen
    mpl.suptitle(title)  # Titel setzen
    mpl.axis('on')  # Achsen einblenden
    mpl.show()


if __name__ == "__main__":
    image_path = "1.png"  # Pfad zum Bild
    image = load_image(image_path)  # Bild laden
    pixel_m = get_stuff_from_image(image)  # Bild in Binärmatrix umwandeln

    kernel = np.array([[-1, 2, -1],[-1, 2, -1],[-1, 2, -1]])  # Kernel definieren

    iteration_count = 4  # Anzahl der Iterationen festlegen
    current_matrix = pixel_m

    # Iterative Verarbeitung und Darstellung der Ergebnisse
    for iteration in range(iteration_count):
        print(f"Iteration {iteration + 1}: Anwenden von make_matrix.")
        current_matrix = make_matrix(current_matrix, image, kernel)  # Faltung mit Kernel
        plot_image(current_matrix, f"Iteration {iteration + 1} - Nach make_matrix")

        print(f"Iteration {iteration + 1}: Anwenden von max_matrix.")
        current_matrix = max_matrix(current_matrix, kernel)  # Maximalwert-Matrix berechnen
        plot_image(current_matrix, f"Iteration {iteration + 1} - Nach max_matrix")

    print("Verarbeitung abgeschlossen.")
