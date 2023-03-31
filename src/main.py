import argparse
import projectlib
from PIL import Image

# Définition des arguments de ligne de commande
parser = argparse.ArgumentParser(description='Réduction en demi-tons d\'une image.')
parser.add_argument('image', type=str, help='nom de l\'image à réduire en demi-tons')
parser.add_argument('algo', type=int, help='la version de l\'algorithme utilisé')

# Analyse des arguments de ligne de commande
args = parser.parse_args()

# Ouverture de l'image
img = Image.open(args.image)
algo = args.algo

#Conversion de l'image en niveaux de gris
img = img.convert('L')

projectlib.switch_algo(algo, img)






