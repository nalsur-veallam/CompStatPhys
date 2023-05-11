import numpy as np
import pylab as plt

data = np.loadtxt('fluid_widom_main.log', skiprows=5)

widom = data[:, -1]
mu = -1.4*np.log(np.mean(np.exp(-widom/1.4)))

err= np.std(data[:, -1]) / np.sqrt(len(data))/np.mean(widom)*mu

print("Widom mu is", mu, "+-", err)
print("Widom mu is", np.mean(data[:, -2]), "+-", np.std(data[:, -2])/np.sqrt(len(data[:,-2])))


data = np.loadtxt('fluid_gcmc_main_-0.93.log', skiprows=6)

fig, _ = plt.subplots()

plt.plot(data[:, 1], data[:, -1])
plt.xlabel('Time')
plt.ylabel('Density')
plt.grid()
fig.savefig("gce.pdf")
