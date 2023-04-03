import lib
import algo_pointCentre
from PIL import Image


def horiz(img, sizeTrame, algo):
    pixels = img.load()

    width, height = img.size
    cpt = 0

    # if (algo == 2):
    #     version =
    # else:
    version = algo_pointCentre.getTrameCentre

    for x in range(0, width, sizeTrame):
        for y in range(0, height, sizeTrame):
            cpt += 1
            zoneIntensity = 0
            change = 0
            sizeTrameX, sizeTrameY = sizeTrame, sizeTrame
            if (x > width-sizeTrame):
                sizeTrameX = width-x
            if (y > height-sizeTrame):
                sizeTrameY = height-y

            for i in range(sizeTrameX):
                for j in range(sizeTrameY):
                    if (pixels[x+i, y+j] != 0 and pixels[x+i, y+j] != 255):
                        change = 1
                    zoneIntensity += pixels[x+i, y+j]/(sizeTrame*sizeTrame)

            if (change == 0):
                continue

            trame = version(zoneIntensity, sizeTrame, lib.paint)

            for i in range(sizeTrameX):
                for j in range(sizeTrameY):
                    pixels[x+i, y+j] = trame[i][j]

    img.save("resources/result.jpg", "jpeg")
