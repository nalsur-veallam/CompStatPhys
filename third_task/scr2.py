import numpy as np
import pylab as plt

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

Ts = [1.4, 1.5]
rhos = [0.61, 0.64, 0.67]    

fig, axs = plt.subplots(2, 3, figsize=(24,12))

k = -1
for rho in rhos:
    k +=1
    i = -1
    for T in Ts:
        i +=1
        ax = axs[i, k]
        data = np.loadtxt('log.vacf.T'+str(T)+'.rho'+str(rho)+'.txt', skiprows=1, max_rows=31323)
        x = data[:, 0]
        y = data[:, 1]
        
        mx, idxs = np.unique(x, return_index=True)
        my = []
        for x_ in mx:
            my.append(np.mean(y[x==x_]))
        
        idxs = np.argsort(x)
        x = x[idxs]
        y = y[idxs]
        
        ax.plot(x, y, alpha=0.3, lw=3)
        ax.plot(mx, my, label='Average', lw=2)
        ax.set_xlabel("$\\tau$", fontsize=16)  
        ax.set_ylabel('АКФС', fontsize=16) 
        ax.grid()
        ax.legend(fontsize=16)
        ax.set_title('T = '+str(T)+' rho = '+str(rho), fontsize=20)
        ax.tick_params(axis='both', which='major', labelsize=16)
        #plt.show()
        
        
fig.savefig('akfs.pdf')
fig, axs = plt.subplots(2, 3, figsize=(24,12))
       
k = -1
for rho in rhos:
    k +=1
    i = -1
    for T in Ts:
        i +=1
        ax = axs[i, k]
        data = np.loadtxt('log.vacf.T'+str(T)+'.rho'+str(rho)+'.txt', skiprows=1, max_rows=31323)
        x = data[:, 0]
        y = 1/3*data[:, 2]
        
        mx, idxs = np.unique(x, return_index=True)
        my = []
        for x_ in mx:
            my.append(np.mean(y[x==x_]))
        
        idxs = np.argsort(x)
        x = x[idxs]
        y = y[idxs]
        
        ax.plot(x, y, alpha=0.3, lw=3)
        ax.plot(mx, my, label='Average', lw=2)
        ax.set_xlabel("$\\tau$", fontsize=16)  
        ax.set_ylabel('D', fontsize=16) 
        ax.grid()
        ax.legend(fontsize=16)
        ax.set_title('T = '+str(T)+' rho = '+str(rho), fontsize=20)
        ax.tick_params(axis='both', which='major', labelsize=16)
        #plt.show()
        
fig.savefig('Dgk.pdf')
