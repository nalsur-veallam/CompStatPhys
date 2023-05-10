import numpy as np
import pylab as plt

Ts = [1.4, 1.5]
rhos = [0.61, 0.64, 0.67]

for rho in rhos:
    for T in Ts:
        data = np.loadtxt('msd.T'+str(T)+'.rho'+str(rho)+'.log', skiprows=1, max_rows=101)
        x = data[:, 0]
        y = data[:, 1]
        n = len(x)
        
        D = (np.sum(x*y)/n - np.sum(x)*np.sum(y)/n**2)/(np.sum(x**2)/n - np.sum(x)**2/n**2)/6
        print("(1) D for T=", T, "and rho=", rho, "is", D)
        
        
print('\n\n\n')

for rho in rhos:
    for T in Ts:
        data = np.loadtxt('msd.T'+str(T)+'.rho'+str(rho)+'.log', skiprows=1, max_rows=101)
        d = data[80:, 2]
        
        D = np.mean(d)
        err = np.std(d)
        print("(2) D for T=", T, "and rho=", rho, "is", D, "+-", err)
        
