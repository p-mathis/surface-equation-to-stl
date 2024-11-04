"""Création d'un fichier stl à partir de l'équation paramétrique d'une surface.
Ce fichier est enregistré en local et peut être visualisé, par exemple avec meshlab
De nombreuses équations paramétriques de surfaces sont disponibles sur le site mathcurve.com"""
"""Creating an stl file from the parametric equation of surfaces.
This file is saved locally and can be viewed, for example with meshlab
Many parametric surface equations are available on the mathcurve.com website"""

import numpy as np
import time

# Noms de dossiers et de fichiers
# Folder and file names
path_folder = "/path/of/your/folder/"
surface_name = "nameOfYourSurfece"

# Initialisation des paramètres u et v
# Vakeurs start et end fonction de la courbe étudiée : ici surface de Mobius
# Initialization of parameters u and v
# Start and end values ​​depending on the curve studied: here 

uStart = 0
uEnd = 100
uSteps = 100
vStart = 0
vEnd = 2*np.pi
vSteps = uSteps

u = np.linspace(uStart, uEnd, uSteps)
v = np.linspace(vStart, vEnd, vSteps)

# Créer la grille de maillage
# Create the meshgrid
U, V = np.meshgrid(u, v)

# Définir X, Y et Z en fonction des paramètres U et V et de diverses constantes
# Exemple pour la surface de Mobius :https://mathcurve.com/surfaces/mobiussurface/mobiussurface.shtml
# Define X, Y and Z as a function of the parameters U and V and various constants
# Example for the Mobius surface: https://mathcurve.com/surfaces.gb/mobiussurface/mobiussurface.shtml

a = 20

X = (a + U*np.cos(V/2)) * np.cos(V)
Y = (a + U*np.cos(V/2)) * np.sin(V)
Z = U * np.sin(V/2)


# Quelques fonctions utiles
# Some useful functions
def allCoordinatesPositives(X, Y, Z):
    """En théorie, un fichier slt ne doit pas contenir de nombre négatifs (ceci n'est plus une règle absolue)"""
    """In theory, a slt file should not contain negative numbers (this is no longer an absolute rule)"""
    xMin = np.min(X)
    yMin = np.min(Y)
    zMin = np.min(Z)
    print(xMin, yMin, zMin)
    if xMin < 0:
        X -= xMin
    if yMin < 0:
        Y -= yMin
    if zMin < 0:
        Z -= zMin
    
    return [X, Y, Z]

def format_e(x):
    """Formate les nombres en écriture scientifique ; 10 chiffres"""
    """Formats numbers in scientific notation; 10 digits"""
    return f'{x:.10e}'

def normalVector(V1, V2):
    """Renvoie le vecteur normal unitaire orthogonal à deux vecteurs initiaux"""
    """Returns the unit normal vector orthogonal to two initial vectors"""
    vector = np.cross(V1, V2)
    norm = np.linalg.norm(vector)
    return vector / norm

def normal_for_facet(facet):
    """facet est un triangle ; points 0, 1 et 2 (dans le sens trigonométrique ?)
    Renvoie le vecteur normé orthogonal à la facette facet"""
    """facet is a triangle; points 0, 1 and 2 (in the counterclockwise direction?)
    Returns the normalized vector orthogonal to the facet facet"""
    p0 = np.asarray(facet[0])
    p1 = np.asarray(facet[1])
    p2 = np.asarray(facet[2])
    V1 = p1 - p0
    V2 = p2 - p0
    return normalVector(V1, V2)

def stringForFacet(facet):
    """Donne le string stl pour une facette facet
    Voir https://en.wikipedia.org/wiki/STL_(file_format)"""
    """Gives the stl string for a facet facet
    See https://en.wikipedia.org/wiki/STL_(file_format)"""

    try:

        string = ""
        normal = normal_for_facet(facet)
        string += f'facet normal {format_e(normal[0])} {format_e(normal[1])} {format_e(normal[2])}\n'
        string += f'    outer loop\n'
        string += f'        vertex {format_e(facet[0][0])} {format_e(facet[0][1])} {format_e(facet[0][2])}\n'
        string += f'        vertex {format_e(facet[1][0])} {format_e(facet[1][1])} {format_e(facet[1][2])}\n'
        string += f'        vertex {format_e(facet[2][0])} {format_e(facet[2][1])} {format_e(facet[2][2])}\n'
        string += f'    endloop\n'
        string += f'endfacet\n'
        return string
    
    except:
        # pour éliminer les erreurs liées à une norme 0
        # to eliminate errors linked to a 0 norm
        pass

# Début du décompte de temps
# Start of time countdown

timeStart = time.time()

# Commenter ou décommenter selon que l'on veut des valeurs X, Y, Z toutes positives
# Comment or uncomment depending on whether you want all positive X, Y, Z values

positivesCoordinates = allCoordinatesPositives(X, Y, Z)
X = positivesCoordinates[0]
Y = positivesCoordinates[1]
Z = positivesCoordinates[2]

# Création du string stl ; lancement de la boucle
# Create the stl string; start the loop

string = f'solid {surface_name}\n'

for i in range(0,len(v)-1):
    for j in range(0,len(u)-1):
        """Si on a quatre points P0, P1, P2 et P3 qui forment un losange tournant dans le sens trigonométrique :
        P0 est en indice i, j
        P1 est en indice i, j+1 
        P2 est en indice i+1, j+1
        P3 est en indice i+1, j
        On crée le deux facettes P0P1P2 et P1P2P3"""

        """If we have four points P0, P1, P2 and P3 which form a diamond rotating in the trigonometric direction:
        P0 is in index i, j
        P1 is in index i, j+1 
        P2 is in index i+1, j+1
        P3 is in index i+1, j
        We create the two facets P0P1P2 and P1P2P3"""

        P0 = [X[i][j], Y[i][j], Z[i][j]]
        P1 = [X[i][j+1], Y[i][j+1], Z[i][j+1]]
        P2 = [X[i+1][j+1], Y[i+1][j+1], Z[i+1][j+1]]
        P3 = [X[i+1][j], Y[i+1][j], Z[i+1][j]]
        facet1 = [P0, P1, P3]
        facet2 = [P1, P2, P3]
        
        try:
            string += stringForFacet(facet1)
            string += stringForFacet(facet2)
        except:
            pass
        
        print(f'i/j : {i}/{j}')
        
string += f'endsolid {surface_name}'

# Ecriture dans un fichier
# Writing to a file

file = f'{path_folder}{surface_name}.stl'
with open(file, 'w') as f:
    f.write(string)

# Calcul du temps Impression de message
# Time calculation Message printing

timeEnd = time.time()
print(f'Done in {round(timeEnd - timeStart, 3)} seconds')
