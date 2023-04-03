import thresholding
import algo_horiz
import algo_vert

def get_sztr():
    return int(input("Saisir la taille d'un element de trame : "))

def switch_algo(algo, img):
	if algo == 1 :
		seuil = thresholding.get_ths()
		thresholding.threshold(img,seuil)
		return
	if algo == 2 :
		sizeTrame = get_sztr()
		algo = int(input("1 pour pointCentre, 2 pour disperse : "))
		algo_horiz.horiz(img,sizeTrame, algo)
		return
	if algo == 3 :
		sizeTrame = get_sztr()
		algo = int(input("1 pour pointCentre, 2 pour disperse : "))
		algo_vert.vert(img,sizeTrame, algo)
		return
	else:
		print('Algorithme inconnu\n')
		return

        