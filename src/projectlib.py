import thresholding
import sdhalftoning

def switch_algo(algo, img):
	if algo == 1 :
		seuil = thresholding.get_ths()
		thresholding.threshold(img,seuil)
	elif algo == 2 :
		sdhalftoning.execute(img)
	else :
		print("rien\n")

        