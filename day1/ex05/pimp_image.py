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


def ft_invert(array) -> np.ndarray:
    """
    Inverts the color of an image
    """
    invertar = 255 - array
    showImage(invertar)


def ft_red(array) -> np.ndarray:
    '''
    Returns the red channel of an image
    using only =, *
    '''
    redar = array.copy()
    redar[:, :, 1] = 0
    redar[:, :, 2] = 0
    showImage(redar)


def ft_green(array) -> np.ndarray:
    '''
    Returns the green channel of an image
    '''
    greenar = array.copy()
    greenar[:, :, 0] = 0
    greenar[:, :, 2] = 0
    showImage(greenar)


def ft_blue(array) -> np.ndarray:
    '''
    Returns the blue channel of an image
    '''
    bluear = array.copy()
    bluear[:, :, 0] = 0
    bluear[:, :, 1] = 0
    showImage(bluear)


def ft_grey(array) -> np.ndarray:
    '''
    Returns the grey channel of an image
    '''
    greyar = array.copy()
    greyar[:, :, 0] = greyar[:, :, 0] * 0.299
    greyar[:, :, 1] = greyar[:, :, 1] * 0.587
    greyar[:, :, 2] = greyar[:, :, 2] * 0.114
    greyar = greyar.sum(axis=2)
    showImage(greyar)


def applyZoom(image: np.ndarray, w: int, h: int, offX=0, offY=0) -> np.ndarray:
    """
    Zooms in or out of an image by a given factor
    """
    print(len(image), len(image[0]))
    newImg = np.zeros((h, w, 1), dtype=np.uint8)
    for y in range(h):
        for x in range(w):
            newImg[y][x] = image[y + offY][x + offX].mean()
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
        newImgArr = applyZoom(image, 400, 400, 450, 100)
        assert newImgArr is not None, "applyZoom returned None"
        print(newImgArr)
        showImage(newImgArr)
        assert image is not None, "ft_load returned None"
    except AssertionError as e:
        print(e)
        exit(1)
