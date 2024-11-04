"""Référence : https://mathcurve.com/surfaces/klein/klein.shtml
Reference : https://mathcurve.com/surfaces.gb/klein/klein.shtml
"""


import facet as fa
import numpy as np
import time

path_folder = ""  
surface_name = "KleinBottle"

uStart = 0
uEnd = 2*np.pi
uSteps = 50
vStart = 0
vEnd = 2*np.pi
vSteps = 50

u = np.linspace(uStart, uEnd, uSteps)
v = np.linspace(vStart, vEnd, vSteps)

U, V = np.meshgrid(u, v)

a = 3
b = 2

# X = (a + b*np.cos(V))*np.cos(U) 
# Y = (a + b*np.cos(V))*np.sin(U)
# Z = b*np.sin(V)*np.cos(U/2)

X = (a + b*(np.cos(U/2)*np.sin(V) - np.sin(U/2)*np.sin(2*V))) * np.cos(U)
Y = (a + b*(np.cos(U/2)*np.sin(V) - np.sin(U/2)*np.sin(2*V))) * np.sin(U)
Z = b* (np.sin(U/2)*np.sin(V) + np.cos(U/2)*np.sin(2*V))

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