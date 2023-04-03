import lib
from PIL import Image


def vert(img, sizeTrame, algo):
    pixels = img.load()

    width, height = img.size
    cpt = 0
    img.save("resources/result.jpg", "jpeg")

