from PIL import Image

def load_image(file_path):
    try:
        img = Image.open(file_path)
        print(f"Image loaded successfully! Format: {img.format}, Size: {img.size}, Mode: {img.mode}")
        return img
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

if __name__ == "__main__":
    image_path = "test_img_1.png" #path to image
    load_image(image_path)
