import thresholding
import sdhalftoning
import algo_pointcentre

def switch_algo(algo, img):
	if algo == 1 :
		seuil = thresholding.get_ths()
		thresholding.threshold(img,seuil)
	elif algo == 2 :
		sizeTrame = algo_pointcentre.get_sztr()
		algo_pointcentre.pointCentre(img,sizeTrame)
	elif algo == 3 :
		sdhalftoning.execute(img)
	else:
		print('Algorithme inconnu\n')

        