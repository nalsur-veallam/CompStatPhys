import numpy as np
import pylab as plt
from numpy import fft as fft
from tqdm import tqdm

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

def acf(data, npts = None):
    """
    Computes time autocorrelation function of a real-valued array `data`.
    """
    
    n = len(data)
    if npts is None:
        npts = n
    npts = min(npts, n)
    dataf = fft.rfft(np.append(data, np.zeros(n)))
    acf = fft.irfft(np.conj(dataf) * dataf)[0:npts]
    for i in range(npts):
        acf[i] /= n - i
    
    return acf[0:npts]

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
        data = np.loadtxt('log.shear.T'+str(T)+'.rho'+str(rho)+'.txt', skiprows=1)
        x = data[:, 0]
        pxy = data[:, 1]
        pxz = data[:, 2]
        pyz = data[:, 3]
        
        ax.plot(x[0:1000], acf(pxy, 1000), lw=3, label='XY')
        ax.plot(x[0:1000], acf(pxz, 1000), lw=3, label='XZ')
        ax.plot(x[0:1000], acf(pyz, 1000), lw=3, label='YZ')
        ax.plot(x[0:1000], 1/3*(acf(pxy, 1000) + acf(pxz, 1000) + acf(pyz, 1000)), lw=3, label='Average')
        ax.set_xlabel("$\\tau$", fontsize=16)  
        ax.set_ylabel('АКФ', fontsize=16) 
        ax.grid()
        ax.legend(fontsize=16)
        ax.set_title('T = '+str(T)+' rho = '+str(rho), fontsize=20)
        ax.tick_params(axis='both', which='major', labelsize=16)
        #plt.show()
        
        
fig.savefig('akfp.pdf')
fig, axs = plt.subplots(2, 3, figsize=(24,12))
       
k = -1
for rho in rhos:
    k +=1
    i = -1
    for T in Ts:
        i +=1
        ax = axs[i, k]
        data = np.loadtxt('log.shear.T'+str(T)+'.rho'+str(rho)+'.txt', skiprows=1)
        x = data[:, 0]
        pxy = data[:, 1]
        pxz = data[:, 2]
        pyz = data[:, 3]
        
        N = len(x) - 1000
        step = 10
        Nsteps = N//step
        
        Is = []
        for p in tqdm(range(Nsteps)):
            intxy, intxz, intyz = integrate(acf(pxy[p*step:p*step+1000], 1000), x[p*step:p*step+1000]), integrate(acf(pxz[p*step:p*step+1000], 1000), x[p*step:p*step+1000]), integrate(acf(pyz[p*step:p*step+1000], 1000), x[p*step:p*step+1000])
            integ=(intxy + intxz + intyz) / 3
            Is.append(np.mean(integ[-100:]))
            
        I = np.mean(Is)
        err = np.std(Is)/np.log(Nsteps)
        
        
        #intxy, intxz, intyz = integrate(acf(pxy, 1000), x[0:1000]), integrate(acf(pxz, 1000), x[0:1000]), integrate(acf(pyz, 1000), x[0:1000])
        #integ=(intxy + intxz + intyz) / 3
        
        #ax.plot(x[0:1000], intxy, lw=3, label='XY')
        #ax.plot(x[0:1000], intxz, lw=3, label='XZ')
        #ax.plot(x[0:1000], intyz, lw=3, label='YZ')
        #ax.plot(x[0:1000], integ, lw=3 , label='Average')
        #ax.set_xlabel("$\\tau$", fontsize=16)  
        #ax.set_ylabel('Интеграл', fontsize=16) 
        #ax.grid()
        #ax.legend(fontsize=16)
        #ax.set_title('T = '+str(T)+' rho = '+str(rho), fontsize=20)
        #ax.tick_params(axis='both', which='major', labelsize=16)
        #plt.show()
        #I = np.mean(integ[-300:])
        eta = 15**3/rho/T*I
        print("$\\eta$ for T=", T, "and rho=", rho, "is", eta, "+-", 15**3/rho/T*err)
        
fig.savefig('ieta.pdf')
