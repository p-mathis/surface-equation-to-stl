"""Référence : https://mathcurve.com/surfaces/mobiussurface/mobiussurface.shtml
Reference : https://mathcurve.com/surfaces.gb/mobiussurface/mobiussurface.shtml
Exemple de surface non fermée. Utilisation de fa.stlAllSurface()
Example of a closed surface. Using fa.stlAllSurface()
"""

import facet as fa
import numpy as np
import time

path_folder = ""  
surface_name = "Mobius"

uStart = 0
uEnd = 100
uSteps = 200
vStart = 0
vEnd = 4*np.pi 
vSteps = uSteps 

u = np.linspace(uStart, uEnd, uSteps)
v = np.linspace(vStart, vEnd, vSteps)

U, V = np.meshgrid(u, v)

a = 20

X = (a + U*np.cos(V/2)) * np.cos(V)
Y = (a + U*np.cos(V/2)) * np.sin(V)
Z = U * np.sin(V/2)

offset = 0.5

timeStart = time.time()

stl = fa.stlAllSurface(X, Y, Z, offset, surface_name)

timeEnd = time.time()
print(f'String stl créé en {round(timeEnd - timeStart, 3)} secondes\nStl string created in {round(timeEnd - timeStart, 3)} seconds')

file = f'{path_folder}{surface_name}.stl'
with open(file, "w") as f:
    f.write(stl)
    
if path_folder == "":
    print(f'Fichier {surface_name}.stl enregistré dans le dossier courant\nFile {surface_name}.stl saved in the current folder')
else:
    print(f'Fichier {surface_name}.stl enregistré dans le dossier {path_folder}\nFile {surface_name}.stl saved in folder {path_folder}')