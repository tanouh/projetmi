import thresholding
import algo_pointcentre

def switch_algo(algo, img):
	if algo == 1 :
		seuil = thresholding.get_ths()
		thresholding.threshold(img,seuil)
	if algo == 2 :
		sizeTrame = algo_pointcentre.get_sztr()
		algo_pointcentre.pointCentre(img,sizeTrame)
	else:
		print('rien\n')

        