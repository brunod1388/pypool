import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """Load an image from a given path and return a numpy array"""
    try:
        image = Image.open(path)
        data = np.asarray(image)
        print("the shape of image is:", data.shape)
    except FileNotFoundError:
        print("File not found")
        return None
    except (ValueError, AttributeError):
        print("Image cannot be converted to a numpy array")
        return None
    return data
