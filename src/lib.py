from PIL import Image

def paint(trame, x, y, base, treshold, cpt):
    if (cpt < treshold):
        trame[x][y] = 255 - base
    else:
        trame[x][y] = base