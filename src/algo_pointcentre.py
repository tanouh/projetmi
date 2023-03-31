from PIL import Image


def get_sztr():
    return int(input("Saisir la taille d'un element de trame : "))


def paint(trame, x, y, base, treshold, cpt):
    if (cpt < treshold):
        trame[x][y] = 255 - base
    else:
        trame[x][y] = base


def getTrame(intensity, sizeZone):
    base = 0
    if (intensity > 127):
        base = 255
    treshold = (abs(base-intensity)/255)*sizeZone*sizeZone
    trame = [[base for i in range(sizeZone+1)] for j in range(sizeZone+1)]
    cx, cy = sizeZone//2, sizeZone//2
    cpt = 1
    m = 1
    paint(trame, cx, cy, base, treshold, cpt)
    cpt += 1
    while (cpt < treshold and cpt < sizeZone*sizeZone):
        for i in range(1-m, m):
            paint(trame, cx+i, cy-m, base, treshold, cpt)
            cpt += 1
        for i in range(1-m, m):
            paint(trame, cx+m, cy+i, base, treshold, cpt)
            cpt += 1
        for i in range(1-m, m):
            paint(trame, cx-i, cy+m, base, treshold, cpt)
            cpt += 1
        for i in range(1-m, m):
            paint(trame, cx-m, cy-i, base, treshold, cpt)
            cpt += 1
        paint(trame, cx-m, cy-m, base, treshold, cpt)
        cpt += 1
        paint(trame, cx+m, cy-m, base, treshold, cpt)
        cpt += 1
        paint(trame, cx+m, cy+m, base, treshold, cpt)
        cpt += 1
        paint(trame, cx-m, cy+m, base, treshold, cpt)
        cpt += 1
        m += 1
    return trame


def pointCentre(img, sizeTrame):
    pixels = img.load()

    width, height = img.size
    # print(width, height)
    cpt = 0

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
            trame = getTrame(zoneIntensity, sizeTrame)

            for i in range(sizeTrameX):
                for j in range(sizeTrameY):
                    pixels[x+i, y+j] = trame[i][j]

    img.save("resources/result.jpg", "jpeg")
