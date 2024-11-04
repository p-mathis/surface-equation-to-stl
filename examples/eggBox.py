"""Référence : https://mathcurve.com/surfaces/boiteaoeufs/boiteaoeufs.shtml
Reference : https://mathcurve.com/surfaces.gb/boiteaoeufs/boiteaoeufs.shtml
"""


import facet as fa
import numpy as np
import time

path_folder = ""  
surface_name = "BoiteAOeufs"

uStart = 0
uEnd = 100
uSteps = 200
vStart = 0
vEnd = 100
vSteps = uSteps

u = np.linspace(uStart, uEnd, uSteps)
v = np.linspace(vStart, vEnd, vSteps)

U, V = np.meshgrid(u, v)

a = 3
b = 2 

# X = (a + b*np.cos(V))*np.cos(U) 
# Y = (a + b*np.cos(V))*np.sin(U)
# Z = b*np.sin(V)*np.cos(U/2)

X = U
Y = V
Z = a * (np.sin(U/b) + np.sin(V/b))

offset = 0.5

timeStart = time.time()

stl = fa.stlOffsetSurface(X, Y, Z, offset, surface_name)

timeEnd = time.time()
print(f'String stl créé en {round(timeEnd - timeStart, 3)} secondes\nStl string created in {round(timeEnd - timeStart, 3)} seconds')

file = f'{path_folder}{surface_name}.stl'
with open(file, "w") as f:
    f.write(stl)
if path_folder == "":
    print(f'Fichier {surface_name}.stl enregistré dans le dossier courant\nFile {surface_name}.stl saved in the current folder')
else:
    print(f'Fichier {surface_name}.stl enregistré dans le dossier {path_folder}\nFile {surface_name}.stl saved in folder {path_folder}')