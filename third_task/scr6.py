import numpy as np
import pylab as plt
from sklearn.linear_model import LinearRegression

rhos =  np.array([[0.61, 0.64, 0.67], [0.61, 0.64, 0.67]]).flatten()
Ts = np.array([[1.4, 1.4, 1.4], [1.5, 1.5, 1.5]]).flatten()
etas = np.array([[0.75, 1.03, 1.11], [1.01, 0.88, 1.28]]).flatten()
s2s = np.array([[0.522, 0.700, 0.78], [0.487, 0.671, 0.748]]).flatten()

etas = etas*rhos**(-2/3)/Ts**(1/2)
exps2 = np.exp(-s2s)

idxs = np.argsort(exps2)
x = exps2[idxs]
y = etas[idxs]

model =  LinearRegression()
model.fit(x.reshape(-1, 1), y)
xs = np.linspace(0.4, 0.7, 100)
ys = model.predict(xs.reshape(-1, 1))

fig, ax = plt.subplots(figsize=(15,12))

ax.scatter(x, y,lw=3)
ax.plot(xs, ys,lw=3)
ax.set_xlabel("exp(-$S_2/k_bT$)", fontsize=16)  
ax.set_ylabel('$\\eta^*$', fontsize=16) 
ax.grid()
ax.tick_params(axis='both', which='major', labelsize=16)
fig.savefig('rosen.pdf')

X = np.array([s2s, s2s**2, s2s**3, s2s**4]).T
model =  LinearRegression()
model.fit(X, y)
xs = np.linspace(0.45, 0.8, 100)
Xs = np.array([xs, xs**2, xs**3, xs**4]).T


fig, ax = plt.subplots(figsize=(15,12))
Ys = model.predict(Xs)
ax.scatter(s2s, etas,lw=3)
ax.plot(xs, Ys,lw=3)
ax.set_xlabel("$S_2/k_bT$", fontsize=16)  
ax.set_ylabel('$\\eta^*$', fontsize=16) 
ax.grid()
ax.tick_params(axis='both', which='major', labelsize=16)
fig.savefig('p4.pdf')

        
