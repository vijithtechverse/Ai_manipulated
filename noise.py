import numpy as np
from PIL import Image

def noise_variance(image_path):
    img = Image.open(image_path).convert("L")
    img = np.array(img)
    return np.var(img)
