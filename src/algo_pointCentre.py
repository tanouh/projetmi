from PIL import Image

def getTrameCentre(intensity, sizeZone, paint):
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