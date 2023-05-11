import csv
import pylab as plt
import numpy as np

from scipy import integrate

ens = []
c= 1e-5
lambdaa_min = np.log(c)
lambdaa_max =  np.log(1+c)
x_i = np.array([0.99573, 0.974554, 0.93243, 0.8707658, 0.79304, 0.70292255,
                0.603892, 0.5, 0.396105,0.29707, 0.206956, 0.129234, 0.067567, 0.025446, 0.004272])

w_i = np.array([0.02293, 0.06309, 0.10479, 0.14065, 0.16900, 0.19035, 0.20443, 0.20948, 0.20443, 0.19035,0.16900, 0.14065,0.10479,0.06309,0.02293])
lambdaa = [lambdaa_min + x*(lambdaa_max - lambdaa_min) for x in x_i]

for i in range(1, 16):
    name = './ti/ti_energy.' + str(i) + '.log'
    arr = []
    with open(name) as f:
        for i, line in enumerate(f):
            if i == 0: continue
            try: arr.append(line.split())
            except Exception as e:
                print(e)
                continue
    en = []
    for i in range(len(arr)):
        en.append(float(arr[i][1]))
    en = np.mean(np.array(en))
    ens.append(en)
    
    
fig, (ax) = plt.subplots()



ax.plot(lambdaa, ens,'o-')
ax.set_xlabel('lambda')
ax.set_ylabel('energy')
ax.grid()
plt.show()
fig.savefig('energy.pdf')


integral = [np.exp(lambdaa[i])/(np.exp(lambdaa[i]) -  c)*ens[i] for i in range(len(lambdaa))]

fig, (ax) = plt.subplots(1, 1)

ax.plot(lambdaa, integral,'o-')
ax.set_xlabel('lambda')
ax.set_ylabel('dU/d lambda')
ax.grid()
plt.show()
fig.savefig('int.pdf')

print("The integral is", integrate.simpson(integral, lambdaa))
integral = [np.exp(lambdaa[i])/(np.exp(lambdaa[i]) -  c)*ens[len(lambdaa) - 1 - i] for i in range(len(lambdaa))]
print("The integral is", np.array(integral).dot(w_i)/(lambdaa_max - lambdaa_min)*2)
