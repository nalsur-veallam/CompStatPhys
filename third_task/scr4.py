import numpy as np
import pylab as plt

Ts = [1.4, 1.5]
rhos = [0.61, 0.64, 0.67]
etas = [[0.823, 1.0183, 1.1457], [0.8618, 0.8737, 1.1394]]
Ds = [[0.213, 0.193, 0.171], [0.227, 0.207, 0.187]]
Rs = []

for i, rho in enumerate(rhos):
    for j, T in enumerate(Ts):
        eta = etas[j][i]
        D = Ds[j][i]
        R = T / 6/np.pi/eta/D
        Rs.append(R)
        print("R for T=", T, "and rho=", rho, "is", R)
        
print("R is", np.mean(Rs), "+-", np.std(Rs))
