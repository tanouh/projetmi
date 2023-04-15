from PIL import Image
import random

#tramage à points dispersés

def getTrameDispersee(intensity, sizeZone, paint, ratio):
    base = 0
    if (intensity > 127):
        base = 255
    treshold = sizeZone * sizeZone * ratio
    trame = [[base for i in range(sizeZone)] for j in range(sizeZone)]
    cpt = 1
    while (cpt < treshold):
        x = random.randint(0, sizeZone - 1)
        y = random.randint(0, sizeZone - 1)
        paint(trame, x, y, base, treshold, cpt)
        cpt += 1
    return trame

