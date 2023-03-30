import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial.distance import jensenshannon
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
import scipy.stats as sps

arr = []
with open("log.mcnvt.txt") as f:
    for line in f:
        #print(float(x) for x in coloumn.split())
        arr.append(line.split())
        
Probs = []
for i in range(14, 114):
    Probs.append(float(arr[i][6]))
    
    
x = np.linspace(0, 20000, 101)
    
fig = plt.figure(figsize=(10,7))     
    
plt.plot(x[1:], Probs,'o-', c='green') 
plt.xlabel('Timesteps')  
plt.ylabel('Probability') 
plt.grid()
plt.show()
fig.savefig("mcprobs.pdf")
