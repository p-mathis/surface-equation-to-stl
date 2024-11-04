[Version Française](#principe)
## Principle
These scripts allow you to create an `stl` file for a surface whose parametric equation is known.  
The `facet` library includes the `Facet()` class and various methods which will, from a set of X, Y and Z coordinates, allow the creation of the `stl` file. The `stlFromXYZ.py` script
creates the `stl` file and saves it locally.  
Using `stlFromXYZ.py` requires importing `facet`; It is also worth checking that `facet` will be accessible, if necessary by modifying the `PYTHONPATH`.  
The `stl` file thus created is written in text mode. Depending on the number of facets created, it may be more or less important. It may then be beneficial to convert it to binary, for example with MeshLab.  
`surface2stl.py` is a script which allows the creation of the `stl` file of a surface without using the `facet` module.
## Usage
In the `stlFromXYZ.py` file:
- Indicate the file saving path. If left empty, the file will be saved in the current folder. Do not omit the terminal `slash` at the end of the path.
- Indicate the name given to the surface.
- Indicate the domain of study of the function by giving the lower and upper limits of the parameters `u` and `v`.
- Indicate the number of steps to establish the mesh grid (`uSteps` and `vSteps`).
- Indicate, if necessary, the variables of the function studied. Enter the values ​​of X, Y and Z using `U` and `V` as parameters in capital letters (`U` and `V` correspond to the mesh grid of `u` and `v`).
- If necessary define an `offset` (see the introduction to `facet.py`)
- Depending on the choice (with or without `offset`) comment or uncomment the lines `stl = fa.stlOffsetSurface(X, Y, Z, offset, surface_name)` and `stl = fa.stlSingleSurface(X, Y, Z, surface_name)`
- Run the script.

## Examples
Various sample scripts are available in the `Examples` folder

<br><br>
[English Version](#principle)


## Principe
Ces scripts permettent de créer un fichier `stl` pour une surface dont on connaît l'équation paramétrique.  
La librairie `facet` comprend la classe `Facet()` et diverses méthodes qui vont, à partir d'un jeu de coordonnées X, Y et Z permettre de créer le fichier `stl`. Le script `stlFromXYZ.py`
crée le fichier `stl` et l'enregistre en local.  
L'utilisation de `stlFromXYZ.py`, nécessite l'import de `facet` ; aussi convient-il de vérifier que `facet`sera accessible, au besoin en modifiant le `PYTHONPATH`.  
Le fichier `stl` ainsi créé est écrit en mode texte. En fonction du nombre de facettes créées, il peut être plus ou moins volumineux. Il peut alors y avoir intérêt à le convertir en binaire, par exemple avec MeshLab.  
`surface2stl.py` est un script qui permet la création du fichier `stl` d'une surface sans utiliser le module `facet`.
## Usage
Dans le fichier `stlFromXYZ.py` :
- Indiquer le chemin d'enregistement du fichier. Si il est laissé vide, le fichier sera enregistré dans le dossier courant. Ne pas omettre le `slash`terminal à la fin du chemin.
- Indiquer le nom donné à la surface.
- Indiquer le domaine d'étude de la fonction en donnant les limites inférieures et supérieures des paramètres `u`et `v`.
- Indiquer le nombre de pas pour établir la grille de maillage (`uSteps`et `vSteps`).
- Indiquer au besoin les variables de la fonction étudiée. Renseigner les valeurs de X, Y et Z en utilisant comme paramètres `U` et `V` en lettres capitales (`U` et `V` correspondent à la grille de maillage de `u` et de `v`).
- Si besoin définir un `offset` (voir l'introduction de `facet.py`)
- En fonction du choix (avec ou sans `offset`) commenter ou décommenter les lignes `stl = fa.stlOffsetSurface(X, Y, Z, offset, surface_name)` et `stl = fa.stlSingleSurface(X, Y, Z, surface_name)`
- Lancer le script.
## Exemples
Divers exemples de scripts sont disponibles dans le dossier `Examples`
<br><br>


