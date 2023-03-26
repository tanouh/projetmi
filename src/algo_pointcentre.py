from PIL import Image


def get_sztr():
    return int(input("Saisir la taille d'un element de trame : "))


def paint(trame, x, y, base, treshold, cpt):
    # print(x, y)
    if (cpt < treshold):
        trame[x][y] = base
    else:
        trame[x][y] = 255 - base
    cpt += 1


def getTrame(x, y, intensity, sizeZone):
    trame = [[0] * sizeZone] * sizeZone
    base = 0
    if (intensity > 127):
        base = 255
    treshold = (intensity/255)*sizeZone*sizeZone
    print("treshold", treshold, "sizeZone//2", sizeZone//2)
    cx, cy = x + sizeZone//2, y + sizeZone//2
    for m in range(sizeZone//2):
        cpt = 0
        print("1m", m)
        for i in range(-m, m+1):
            print(i)
            paint(trame, cx+i, cy+m, base, treshold, cpt)
        print("2m", m)
        for i in range(m, -m-1, -1):
            print(i)
            paint(trame, cx+m, cy+i, base, treshold, cpt)
        print("3m", m)
        for i in range(-m, m+1):
            print(i)
            paint(trame, cx+i, cy+m, base, treshold, cpt)
        print("4m", m)
        for i in range(m, -m-1, -1):
            print(i)
            paint(trame, cx+m, cy+i, base, treshold, cpt)
    return trame


def pointCentre(img, sizeTrame):
    pixels = img.load()

    width, height = img.size
    print(width, height)

    for x in range(0, width-sizeTrame, sizeTrame):
        for y in range(0, height-sizeTrame, sizeTrame):
            zoneIntensity = 0
            for i in range(sizeTrame):
                for j in range(sizeTrame):
                    zoneIntensity += pixels[x+i, y+j]/sizeTrame
            print("intensity", x, y, zoneIntensity)
            trame = getTrame(x, y, zoneIntensity, sizeTrame)
            for i in range(sizeTrame):
                for j in range(sizeTrame):
                    pixels[x+i, y+j] = trame[i][j]
    img.show()
