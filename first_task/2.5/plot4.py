import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial.distance import jensenshannon
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
import scipy.stats as sps

ts = 1.9839715184496334
nbins=50

arr = []
with open("log.mdnvt.txt") as f:
    for line in f:
        #print(float(x) for x in coloumn.split())
        arr.append(line.split())
Nen = []
Ntemp = []
for i in range(4, 105):
    Nen.append(float(arr[i][2]))
    Ntemp.append(float(arr[i][1]))

arr = []    
with open("log.langevin.txt") as f:
    for line in f:
        #print(float(x) for x in coloumn.split())
        arr.append(line.split())
Len = []
Ltemp = []
for i in range(4, 105):
    Len.append(float(arr[i][2]))
    Ltemp.append(float(arr[i][1]))

arr = []    
with open("log.berendsen.txt") as f:
    for line in f:
        #print(float(x) for x in coloumn.split())
        arr.append(line.split())
Ben = []
Btemp = []
for i in range(4, 105):
    Ben.append(float(arr[i][2]))
    Btemp.append(float(arr[i][1]))

arr = []    
with open("log.mcnvt.txt") as f:
    for line in f:
        #print(float(x) for x in coloumn.split())
        arr.append(line.split())
Men = []
Mtemp = []
for i in range(13, 114):
    Men.append(float(arr[i][2]))
    Mtemp.append(float(arr[i][1]))
    
    
print("Nose Energy:", np.mean(Nen), np.std(Nen))
print("Nose Temp:", np.mean(Ntemp), np.std(Ntemp), '\n')
print("Langevin Energy:", np.mean(Len), np.std(Len))
print("Langevin Temp:", np.mean(Ltemp), np.std(Ltemp), '\n')
print("Berendsen Energy:", np.mean(Ben), np.std(Ben))
print("Berendsen Temp:", np.mean(Btemp), np.std(Btemp), '\n')
print("MC Energy:", np.mean(Men), np.std(Men))
print("MC Temp:", np.mean(Mtemp), np.std(Mtemp), '\n')









