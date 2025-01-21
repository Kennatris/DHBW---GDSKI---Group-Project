from PIL import Image

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
    pixel = [[0 for _ in range(width)] for _ in range(height)]
    print(f"Width: {width}, Height: {height}")

    for j in range(height):  # Rows
        for i in range(width):  # Columns
            pixel[j][i] = img.getpixel((i, j))
            print(f"Pixel[{j}][{i}]: {pixel[j][i]}")

    print("Image processing completed.")

if __name__ == "__main__":
    image_path = "test_img_1.png"  # Path to image
    image = load_image(image_path)
    get_stuff_from_image(image)
