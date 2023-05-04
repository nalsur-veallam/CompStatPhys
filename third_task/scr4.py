import numpy as np
import pylab as plt

Ts = [1.4, 1.5]
rhos = [0.61, 0.64, 0.67]
etas = [[0.75, 1.03, 1.11], [1.01, 0.88, 1.28]]
Ds = [[0.213, 0.193, 0.171], [0.227, 0.207, 0.187]]

for i, rho in enumerate(rhos):
    for j, T in enumerate(Ts):
        eta = etas[j][i]
        D = Ds[j][i]
        R = T / 6/np.pi/eta/D
        print("R for T=", T, "and rho=", rho, "is", R)
        
