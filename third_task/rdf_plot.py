import csv
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)



Ts = [1.4, 1.5]
rhos = [0.61, 0.64, 0.67]

fig, axs = plt.subplots(2, 3, figsize=(24,12))
       
k = -1
for rho in rhos:
    k +=1
    j = -1
    for T in Ts:
        j +=1
        ax = axs[j, k]
        arr = []
        with open('rdf.T'+str(T)+'.rho'+str(rho)+'.txt') as f:
            for line in f:
                if line.split()[0]=='#': continue 
                #print(float(x) for x in coloumn.split())
                arr.append(line.split())
        x = []
        y = []

        for i in range(len(arr)):
            x.append(float(arr[i][0]))
            y.append(float(arr[i][1]))




        ax.plot(x, y,'o-', label='rdf',  lw=3)
        ax.set_xlabel("r", fontsize=16)  
        ax.set_ylabel('RDF', fontsize=16) 
        ax.grid()
        ax.legend(fontsize=16)
        ax.set_title('T = '+str(T)+' rho = '+str(rho), fontsize=20)
        ax.tick_params(axis='both', which='major', labelsize=16)
        
        
fig.savefig('rdf.pdf')
