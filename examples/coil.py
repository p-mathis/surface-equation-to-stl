"""Référence : https://mathcurve.com/surfaces/selle/selle.shtml
Reference : https://mathcurve.com/surfaces.gb/selle/selle.shtml
"""


import facet as fa
import numpy as np
import time

path_folder = ""  
surface_name = "Serpentin"

uStart = 0
uEnd = 16*np.pi
uSteps = 500
vStart = 0
vEnd = 2*np.pi
vSteps = 100

u = np.linspace(uStart, uEnd, uSteps)
v = np.linspace(vStart, vEnd, vSteps)

U, V = np.meshgrid(u, v)

a = 3
b = 0.5
h = 0.33

den = 1/((a*a + h*h)**(1/2))
X = (a-b*np.cos(V))*np.cos(U) + b*h*den*np.sin(U)*np.sin(V)
Y = (a-b*np.cos(V))*np.sin(U) - b*h*den*np.cos(U)*np.sin(V)
Z = h*U + b*a*den*np.sin(V)

offset = 0.2

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