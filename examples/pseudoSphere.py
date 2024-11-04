"""Référence : https://mathcurve.com/surfaces/pseudosphere/pseudosphere.shtml
Reference : https://mathcurve.com/surfaces.gb/pseudosphere/pseudosphere.shtml
"""


import facet as fa
import numpy as np
import time

path_folder = ""  
surface_name = "PseudoSphere"

uStart = 0
uEnd = 4
uSteps = 200
vStart = 0
vEnd = 2*np.pi
vSteps = uSteps

u = np.linspace(uStart, uEnd, uSteps)
v = np.linspace(vStart, vEnd, vSteps)

U, V = np.meshgrid(u, v)

a = 12

X = a * np.cos(V) / np.cosh(U)
Y = a * np.sin(V) / np.cosh(U)
Z = a * (U - np.tanh(U))

timeStart = time.time()

stl = fa.stlSingleSurface(X, Y, Z, surface_name)

timeEnd = time.time()
print(f'String stl créé en {round(timeEnd - timeStart, 3)} secondes\nStl string created in {round(timeEnd - timeStart, 3)} seconds')

file = f'{path_folder}{surface_name}.stl'
with open(file, "w") as f:
    f.write(stl)
if path_folder == "":
    print(f'Fichier {surface_name}.stl enregistré dans le dossier courant\nFile {surface_name}.stl saved in the current folder')
else:
    print(f'Fichier {surface_name}.stl enregistré dans le dossier {path_folder}\nFile {surface_name}.stl saved in folder {path_folder}')