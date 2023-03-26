def get_ths():
	return int(input("Saisir la valeur du seuil [entre 0 et 255]: "))

def threshold(img,seuil):
	# Réduction en demi-tons
	pixels = img.load()
	for i in range(img.size[0]):
		for j in range(img.size[1]):
			if pixels[i,j] < seuil:
				pixels[i,j] = 0
			else:
				pixels[i,j] = 255

	# Affichage de l'image résultante
	img.show()