import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial.distance import jensenshannon
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
import scipy.stats as sps

ts = 1.9839715184496334
nbins=50

arr = []
with open("log.berendsen.txt") as f:
    for line in f:
        #print(float(x) for x in coloumn.split())
        arr.append(line.split())
Ben = []
Bpress = []
Bp_all = []
for i in range(4, 105):
    Ben.append(float(arr[i][2]))
    Bpress.append(float(arr[i][3]))
    Bp_all.append(float(arr[i][4]))
    
    
arr = []
with open("log.langevin.txt") as f:
    for line in f:
        #print(float(x) for x in coloumn.split())
        arr.append(line.split())
Len = []
Lpress = []
Lp_all = []
for i in range(4, 105):
    Len.append(float(arr[i][2]))
    Lpress.append(float(arr[i][3]))
    Lp_all.append(float(arr[i][4]))
    
arr = []
with open("log.mdnvt.txt") as f:
    for line in f:
        #print(float(x) for x in coloumn.split())
        arr.append(line.split())
Nen = []
Npress = []
Np_all = []
for i in range(4, 105):
    Nen.append(float(arr[i][2]))
    Npress.append(float(arr[i][3]))
    Np_all.append(float(arr[i][4]))
    
arr = []
with open("log.mcnvt.txt") as f:
    for line in f:
        #print(float(x) for x in coloumn.split())
        arr.append(line.split())
Men = []
Mpress = []
Mp_all = []
for i in range(13, 114):
    Men.append(float(arr[i][2]))
    Mpress.append(float(arr[i][3]))
    Mp_all.append(float(arr[i][4]))


fig = plt.figure(figsize=(10,7)) 

#print("Nose:", np.mean(Npress), np.std(Npress)/np.sqrt(100)*ts, np.std(Npress))
#print("Langevin:", np.mean(Lpress), np.std(Lpress)/np.sqrt(100)*ts, np.std(Lpress))
#print("MC:", np.mean(Mpress), np.std(Mpress)/np.sqrt(100)*ts, np.std(Mpress))
#print("bERENDSEN:", np.mean(Bpress), np.std(Bpress)/np.sqrt(100)*ts, np.std(Bpress))

print("Nose:", np.mean(Nen), np.std(Nen)/np.sqrt(100)*ts, np.std(Nen))
print("Langevin:", np.mean(Len), np.std(Len)/np.sqrt(100)*ts, np.std(Len))
print("MC:", np.mean(Men), np.std(Men)/np.sqrt(100)*ts, np.std(Men))
print("bERENDSEN:", np.mean(Ben), np.std(Ben)/np.sqrt(100)*ts, np.std(Ben))

x = np.linspace(0, 20000, 101)

#for i, intensity1 in enumerate([Bpress, Npress, Mpress, Lpress]):
    #for j, intensity2 in enumerate([Bpress, Npress, Mpress, Lpress]):
        
        #min_ = np.min([intensity1, intensity2])
        #max_ = np.max([intensity1, intensity2])
        
        #probs1 = np.histogram(intensity1, bins=nbins, range=[min_, max_])[0]
        #probs2 = np.histogram(intensity2, bins=nbins, range=[min_, max_])[0]
        #print(" Jensen-Shannon distance for", i, "and", j, "is", jensenshannon(probs1, probs2), '\n')

plt.plot(x, Len,'o-', c='r', label='Langevin' )
plt.plot(x, Men,'o-', c='b', label='Monte-Carlo' ) 
plt.plot(x, Ben,'o-', c='g', label='Berendsen' ) 
plt.plot(x, Nen,'o-', c='gold', label='Nose-Guver' ) 
plt.xlabel('Timesteps')  
plt.ylabel('Energy') 
plt.legend()
plt.grid()
plt.show()
fig.savefig("energies.pdf")


#for i, intensity1 in enumerate([Bpress, Npress, Mpress, Lpress]):
    #for j, intensity2 in enumerate([Bpress, Npress, Mpress, Lpress]):
        
        #print(" mannwhitneyu for", i, "and", j, "is",sps.mannwhitneyu(intensity1, intensity2), '\n')
