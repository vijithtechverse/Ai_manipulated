from PIL import Image, ImageChops, ImageEnhance
import numpy as np

def perform_ela(image, quality=90):
    temp_path = "temp.jpg"
    image.save(temp_path, "JPEG", quality=quality)
    compressed = Image.open(temp_path)

    ela_image = ImageChops.difference(image, compressed)
    enhancer = ImageEnhance.Brightness(ela_image)
    ela_image = enhancer.enhance(10)

    ela_score = np.mean(np.array(ela_image))
    return ela_score, ela_image
