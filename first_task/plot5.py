import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial.distance import jensenshannon
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
import scipy.stats as sps
from sklearn.linear_model import LinearRegression

Nen = np.array([-6.86637279, -4.1543983396039, -3.1592105069, -1.732386799, -0.645371, 0.16912027, 1.5499721327, 2.7813208326732, 3.687071050, 4.89530555841])
Nden = np.array([0.015972102888, 0.13269657920154, 0.2202357, 0.27450810, 0.327414, 0.40656953, 0.459287943, 0.5133357, 0.550053104, 0.614926795])

Len = np.array([-6.86373462970, -4.1485685435643, -3.171459231, -1.7662353, 0.327414, 0.43524455, 1.5172517, 2.572487654, 3.6676281920, 4.67013619])
Lden = np.array([0.01761092161, 0.12823066666727, 0.19503472, 0.25647562, 0.31986526, 0.428014340411, 0.447072059, 0.583915270, 0.58154388, 0.658204911])

Ben = np.array([-6.866227199, -4.130253762376, -3.161928275, -1.7555342089, -0.625837584, 0.476844706, 1.562987129, 2.6278427495, 3.680134173, 4.7334622128])
Bden = np.array([0.00361249, 0.04134750361311, 0.04353499, 0.051585,  0.058745, 0.07148880606, 0.067619131, 0.09300095585, 0.085629671, 0.10011455])

Men = np.array([-6.8584001069306, -4.17643320396, -3.083177424, -1.7795714089, -0.58911271148, 0.79872, 1.072199722277, 2.767432551, 4.0356413108, 5.49403026])
Mden = np.array([0.00930319, 0.085560776854548, 0.1238359534,  0.152028, 0.195947, 0.23623733, 0.26381368, 0.2964733, 0.34865854, 0.3387504490])

Ndtemp = np.array([0.0075409952192, 0.07147318073, 0.110311554, 0.1413785438, 0.16912027, 0.233812311, 0.26017487, 0.2752241958, 0.3113107302, 0.36418265])
Ldtemp = np.array([0.0073829, 0.067607553700, 0.0973286388, 0.13832697, 0.164430135, 0.21368242319, 0.254605586, 0.292263153336,0.334843876, 0.3687763230])
Bdtemp = np.array([0.00402766212, 0.04455526778939, 0.0588449967, 0.073555872, 0.09586010, 0.1237713062, 0.1463594551487, 0.145501128, 0.1729972165, 0.1980037610])

T = np.array([0.1, 1, 1.4, 2, 2.5, 3, 3.5, 4, 4.5, 5])


#fig = plt.figure(figsize=(10,7))     
    
#plt.plot(T, Ldtemp,'o-', c='r', label='Langevin' ) 
#plt.plot(T, Bdtemp,'o-', c='g', label='Berendsen' ) 
#plt.plot(T, Ndtemp,'o-', c='gold', label='Nose-Hoover' ) 
#plt.xlabel('Temperature')  
#plt.ylabel('Temperature fluctuations') 
#plt.legend()
#plt.grid()
#plt.show()
#fig.savefig("tfluct.pdf")


#fig = plt.figure(figsize=(10,7))     
    
#plt.plot(T, Lden,'o-', c='r', label='Langevin' ) 
#plt.plot(T, Bden,'o-', c='g', label='Berendsen' ) 
#plt.plot(T, Nden,'o-', c='gold', label='Nose-Hoover' ) 
#plt.plot(T, Mden,'o-', c='b', label='Monte-Carlo' ) 
#plt.xlabel('Temperature')  
#plt.ylabel('Energy fluctuations') 
#plt.legend()
#plt.grid()
#plt.show()
#fig.savefig("Efluct.pdf")

#fig = plt.figure(figsize=(10,7))
#plt.plot(T, Len,'o-', c='r', label='Langevin' ) 
#plt.plot(T, Ben,'o-', c='g', label='Berendsen' ) 
#plt.plot(T, Nen,'o-', c='gold', label='Nose-Hoover' ) 
#plt.plot(T, Men,'o-', c='b', label='Monte-Carlo' ) 
#plt.xlabel('Temperature')  
#plt.ylabel('Energy') 
#plt.legend()
#plt.grid()
#plt.show()
#fig.savefig("Energy.pdf")


lin = LinearRegression()

X = T.reshape(-1, 1)
for Y in [Bden, Nden, Mden, Lden]:
    lin.fit(X, Y)
    print(lin.coef_**2*125)
