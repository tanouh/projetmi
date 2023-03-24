import thresholding.py

def switch_algo(algo, img):
	if algo == 1 :
		seuil = thresholding.get_ths()
		thresholding.threshold(img,seuil)
	else:
		print('rien\n')

        