import thresholding
import prepare_image

def get_sztr():
    return int(input("Saisir la taille d'un element de trame : "))

def switch_algo(algo, img):
	if algo == 1 :
		seuil = thresholding.get_ths()
		thresholding.threshold(img,seuil)
		return
	if algo == 2 :
		sizeTrame = get_sztr()
		format = int(input("1 pour vert, 2 pour diag : "))
		algo = int(input("1 pour pointCentre, 2 pour disperse : "))
		prepare_image.cut_img(img,sizeTrame, format, algo)
		return
	else:
		print('Algorithme inconnu\n')
		return

        