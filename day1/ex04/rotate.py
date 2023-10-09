import sys
from load_image import ft_load
import numpy as np
from matplotlib import pyplot as plt


def showImage(image: np.ndarray):
    """
    Show an image using matplotlib
    """
    plt.imshow(image, cmap=plt.cm.gray)
    plt.show()


def rotate(image: np.ndarray, w: int, h: int, offX=0, offY=0) -> np.ndarray:
    """
    Zooms in or out of an image by a given factor
    """
    print(len(image), len(image[0]))
    newImg = np.zeros((h, w, 1), dtype=np.uint8)
    for y in range(h):
        for x in range(w):
            newImg[x][y] = image[y + offY][x + offX].mean()
    print("New shape after slicing:", newImg.shape)
    return newImg


if __name__ == "__main__":
    args = sys.argv
    if len(args) == 1:
        exit(0)
    try:
        assert len(args) == 2, "Wrong number of args"
        image = ft_load(args[1])
        showImage(image)
        print(image)
        newImgArr = rotate(image, 400, 400, 450, 100)
        assert newImgArr is not None, "applyZoom returned None"
        print(newImgArr)
        showImage(newImgArr)
        assert image is not None, "ft_load returned None"
    except AssertionError as e:
        print(e)
        exit(1)
