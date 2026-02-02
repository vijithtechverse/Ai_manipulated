import numpy as np

def noise_variance(image):
    """
    image: PIL.Image.Image
    """
    img = image.convert("L")
    img = np.array(img)
    return np.var(img)
