"""Creating an stl file from the parametric equation of surfaces.
This file is saved locally and can be viewed, for example with meshlab
Many parametric surface equations are available on the mathcurve.com website
Requires import of facet module"""
"""Création d'un fichier stl à partir de l'équation paramétrique d'une surface.
Ce fichier est enregistré en local et peut être visualisé, par exemple avec meshlab
De nombreuses équations paramétriques de surfaces sont disponibles sur le site mathcurve.com
Nécessite l'import du module facet"""

import facet as fa
import numpy as np
import time

# Noms de dossiers et de fichiers d'enregistrement du stl
# Folder and file names saving the stl
path_folder = "/path/of/your/folder/to/register/the/file/"  # avec le slash final ; peut être vide --- with trailing slash; may be empty
surface_name = "nameOfYourSurfece"

# Initialisation des paramètres u et v
# Vakeurs start et end fonction de la courbe étudiée : ici surface de Mobius
# Initialization of parameters u and v
# Start and end values ​​depending on the curve studied: here 

uStart = 0
uEnd = 100
uSteps = 200
vStart = 0
vEnd = 4*np.pi 
vSteps = uSteps        # Modifier si besoin / Edit if necessary

u = np.linspace(uStart, uEnd, uSteps)
v = np.linspace(vStart, vEnd, vSteps)

# Créer la grille de maillage
# Create the meshgrid
U, V = np.meshgrid(u, v)

# Définir X, Y et Z en fonction des paramètres U et V et de diverses constantes
# Exemple pour la surface de Mobius :https://mathcurve.com/surfaces/mobiussurface/mobiussurface.shtml
# Define X, Y and Z as a function of the parameters U and V and various constants
# Example for the Mobius surface: https://mathcurve.com/surfaces/mobiussurface/mobiussurface.shtml

a = 20

X = (a + U*np.cos(V/2)) * np.cos(V)
Y = (a + U*np.cos(V/2)) * np.sin(V)
Z = U * np.sin(V/2)

# Définir l'offset si besoin
# Define the offset if necessary
offset = 0.5

# Calcul du temps
# Time calculation
timeStart = time.time()

# Commenter ou décommenter selon le choix : avec offset ou sans offset
# Comment or uncomment depending on the choice: with offset or without offset
stl = fa.stlOffsetSurface(X, Y, Z, offset, surface_name)
# stl = fa.stlSingleSurface(X, Y, Z, surface_name)

# Calcul du temps
# Time calculation
timeEnd = time.time()
print(f'String stl créé en {round(timeEnd - timeStart, 3)} secondes\nStl string created in {round(timeEnd - timeStart, 3)} seconds')

# Écriture dans le fichier
# Writing to file
file = f'{path_folder}{surface_name}.stl'
with open(file, "w") as f:
    f.write(stl)

# Message de fin
# Ending message
if path_folder == "":
    print(f'Fichier {surface_name}.stl enregistré dans le dossier courant\nFile {surface_name}.stl saved in the current folder')
else:
    print(f'Fichier {surface_name}.stl enregistré dans le dossier {path_folder}\nFile {surface_name}.stl saved in folder {path_folder}')
