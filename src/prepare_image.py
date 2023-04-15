import lib
import algo_diag
import algo_pointCentre
import algo_pointDisperse
from PIL import Image


def cut_img(img, sizeTrame, format, algo):
    pixels = img.load()

    width, height = img.size
    cpt = 0

    print(width,height)
    if (format == 2):
        version = algo_diag.getTrameDiag
        ratio = 2
    else:
        ratio = 1 
        if (algo == 1) :
             version = algo_pointCentre.getTrameCentre
        else: 
            version = algo_pointDisperse.getTrameDispersee      
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
                    zoneIntensity += pixels[x+i, y+j]/(sizeTrame*sizeTrame)

            trame = version(zoneIntensity, sizeTrame, lib.paint, ratio)

            for i in range(sizeTrameX):
                for j in range(sizeTrameY):
                    pixels[x+i, y+j] = trame[i][j]

    img.save("resources/resultbis.jpg", "jpeg")
