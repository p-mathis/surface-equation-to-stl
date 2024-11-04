"""Référence : https://mathcurve.com/surfaces/mobius/mobius.shtml
Reference : https://mathcurve.com/surfaces.gb/mobius/mobius.shtml
"""


import facet as fa
import numpy as np
import time

path_folder = ""  
surface_name = "MobiusStrip"

uStart = 0.6
uEnd = 1
uSteps = 200
vStart = 0
vEnd = 2*np.pi
vSteps = uSteps

u = np.linspace(uStart, uEnd, uSteps)
v = np.linspace(vStart, vEnd, vSteps)

U, V = np.meshgrid(u, v)

X = (3*(U**2)*(U**2-1) - 6*U*(1+U**4)*np.cos(V) + (U**6-1)*(4*(np.cos(V))**2 - 1)) * np.sin(V) / (3*U**3)
Y = (4*(1-U**6)*(np.cos(V))**3 - 3*U*(1+U**4) + 3*(U**2 - 1)*(1+U**4)*np.cos(V) + 6*U*(1+U**4)*(np.cos(V))**2) / (3*U**3)
Z = 2 * np.sin(V) * (U**2 - 1) / U

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