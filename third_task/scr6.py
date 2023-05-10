import numpy as np
import pylab as plt
from sklearn.linear_model import LinearRegression

rhos =  np.array([[0.61, 0.64, 0.67], [0.61, 0.64, 0.67]]).flatten()
Ts = np.array([[1.4, 1.4, 1.4], [1.5, 1.5, 1.5]]).flatten()
etas = np.array([[0.823, 1.0183, 1.1457], [0.8618, 1.018, 1.1394]]).flatten()
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
ax.set_ylabel('$eta^*$', fontsize=16) 
ax.grid()
ax.tick_params(axis='both', which='major', labelsize=16)
fig.savefig('rosen.pdf')

X4 = np.array([s2s, s2s**2, s2s**3, s2s**4]).T
X3 = np.array([s2s, s2s**2, s2s**3]).T
X2 = np.array([s2s, s2s**2]).T
model4 =  LinearRegression()
model3 =  LinearRegression()
model2 =  LinearRegression()
model4.fit(X4, np.log(y))
model3.fit(X3, np.log(y))
model2.fit(X2, np.log(y))
xs = np.linspace(0.45, 0.8, 100)
Xs4 = np.array([xs, xs**2, xs**3, xs**4]).T
Xs3 = np.array([xs, xs**2, xs**3]).T
Xs2 = np.array([xs, xs**2]).T


fig, ax = plt.subplots(figsize=(15,12))
Ys4 = model4.predict(Xs4)
Ys3 = model3.predict(Xs3)
Ys2 = model2.predict(Xs2)
ax.scatter(s2s, np.log(etas),lw=3)
ax.plot(xs, Ys4,lw=3, label="$ln(eta^*) = P_4(S_2/k_bT)$")
ax.legend()
ax.set_xlabel("$S_2/k_bT$", fontsize=16)  
ax.set_ylabel('$ln(eta^*)$', fontsize=16) 
ax.grid()
ax.tick_params(axis='both', which='major', labelsize=16)
fig.savefig('p4.pdf')

        
