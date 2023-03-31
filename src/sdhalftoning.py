from PIL import Image

#tramage à points dispersés

def execute(img):
	# Conversion en niveau de gris
	img = img.convert("L")

	# Définition de la taille de la grille de points
	grid_size = 10

	# Création d'une nouvelle image pour le tramage
	new_img = Image.new("1", (img.width, img.height))

	# Boucle sur chaque pixel de l'image
	for x in range(img.width):
		for y in range(img.height):
			# Récupération de la valeur de luminosité du pixel
			lum = img.getpixel((x, y))

			# Calcul de la valeur moyenne de la grille de points
			avg_lum = sum([img.getpixel((i, j)) for i in range(x, x+grid_size) for j in range(y, y+grid_size)]) // (grid_size ** 2)

			# Si la valeur moyenne est supérieure ou égale à la luminosité du pixel, le point est noir
			if avg_lum >= lum:
				new_img.putpixel((x, y), 1)
			# Sinon, le point est blanc
			else:
				new_img.putpixel((x, y), 0)

	# Sauvegarde de l'image tramee
	new_img.show()
