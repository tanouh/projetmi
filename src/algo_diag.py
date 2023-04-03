import algo_pointCentre


def getTrameDiag(intensity, sizeZone, paint, ratio):
    base = 0
    if (intensity > 127):
        base = 255
        trame_a = [[base for i in range((sizeZone//2)+1)]
                   for j in range(sizeZone+1)]
        trame_b = algo_pointCentre.getTrameCentre(
            intensity, sizeZone//2, paint, ratio)
    else:
        trame_a = algo_pointCentre.getTrameCentre(
            intensity, sizeZone//2, paint, ratio)
        trame_b = [[base for i in range((sizeZone//2)+1)]
                   for j in range(sizeZone+1)]

    trame = [[base for i in range(sizeZone+1)] for j in range(sizeZone+1)]

    for x in range(sizeZone):
        for y in range(sizeZone):
            if (base == 0):
                if (x < sizeZone//2 and y < sizeZone//2):
                    trame[x][y] = trame_a[x][y]
                if (x >= sizeZone//2 and y >= sizeZone//2):
                    trame[x][y] = trame_a[x-sizeZone//2][y-sizeZone//2]
            if (base == 255):
                if (x < sizeZone//2 and y >= sizeZone//2):
                    trame[x][y] = trame_b[x][y-sizeZone//2]
                if (x >= sizeZone//2 and y < sizeZone//2):
                    trame[x][y] = trame_b[x-sizeZone//2][y]
    
    return trame
