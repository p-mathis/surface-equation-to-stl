"""Référence : https://mathcurve.com/surfaces/cycliddedupin/cyclidededupin.shtml
Reference : https://mathcurve.com/surfaces.gb/cycliddedupin/cyclidededupin.shtml
Exemple de surface fermée. Utilisation de fa.stlSingleSurface()
Example of a closed surface. Using fa.stlSingleSurface()
"""


import facet as fa
import numpy as np
import time

path_folder = ""  
surface_name = "Dupin"

uStart = 0
uEnd = 2*np.pi
uSteps = 500
vStart = 0
vEnd = 2*np.pi 
vSteps = uSteps 

u = np.linspace(uStart, uEnd, uSteps)
v = np.linspace(vStart, vEnd, vSteps)

U, V = np.meshgrid(u, v)

a = 2
b = 1.7
c = abs(a*a - b*b)**(1/2)
d = 1.7

X =  (d*(c - a*np.cos(U)*np.cos(V)) + b*b*np.cos(U)) / (a - c*np.cos(U)*np.cos(V))
Y =  (b*np.sin(U) * (a - d*np.cos(V))) / (a - c*np.cos(U)*np.cos(V))
Z = (b*np.sin(V) * (c*np.cos(U) - d)) / (a - c*np.cos(U)*np.cos(V)) 

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