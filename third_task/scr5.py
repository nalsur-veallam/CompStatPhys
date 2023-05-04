import numpy as np
import pylab as plt

Ts = [1.4, 1.5]
rhos = [0.61, 0.64, 0.67]

def integrate(ydata, xdata = None):
    """
    Computes running integral of `ydata` using `xdata` as abscissae.
    """
    
    n = len(ydata)
    if xdata is None:
        xdata = range(n)
    
    integ = np.zeros(n)
    for i in range(1,n):
        integ[i] = integ[i-1] + (ydata[i-1] + ydata[i]) / 2 * (xdata[i] - xdata[i-1])
    
    return integ
fig, ax = plt.subplots(figsize=(15,12))

k = -1
for rho in rhos:
    k +=1
    j = -1
    for T in Ts:
        j +=1
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
            
        x= np.array(x)
        y = np.array(y)
        
        x, y = x[y!=0], y[y!=0]
            
        y = x**2 * (y*np.log(y) - (y - 1))
        
        integ = 2*np.pi * rho*integrate(ydata=y, xdata=x)
        I = np.mean(integ[-100:])
        print("I for T=", T, "and rho=", rho, "is", I)
        
        ax.plot(x, integ, lw=3, label='T = '+str(T)+' rho = '+str(rho))
        

ax.set_xlabel("r", fontsize=16)  
ax.set_ylabel('Integral', fontsize=16) 
ax.grid()
ax.legend(fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)
fig.savefig('s2.pdf')
        
