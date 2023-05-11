import numpy as np

data = np.loadtxt("log.l1.4", skiprows=35)

print("(1.4) Pressure is", np.mean(data[:, -1]), "+-", np.std(data[:, -1])/np.sqrt(len(data[:, -1])))
print("(1.4) Temperature is", np.mean(data[:, 1]), "+-", np.std(data[:, 1])/np.sqrt(len(data[:, 1])))

data = np.loadtxt("log.l1.5", skiprows=35)

print("(1.5) Pressure is", np.mean(data[:, -1]), "+-", np.std(data[:, -1])/np.sqrt(len(data[:, -1])))
print("(1.5) Temperature is", np.mean(data[:, 1]), "+-", np.std(data[:, 1])/np.sqrt(len(data[:, 1])))

data = np.loadtxt("log.1.4", skiprows=36)

print("(1.4 after nph) Pressure is", np.mean(data[:, -2]), "+-", np.std(data[:, -2])/np.sqrt(len(data[:, -2])))
print("(1.4 after nph) Temperature is", np.mean(data[:, 1]), "+-", np.std(data[:, 1])/np.sqrt(len(data[:, 1])))

data = np.loadtxt("log.1.5", skiprows=36)

print("(1.5 after nph) Pressure is", np.mean(data[:, -2]), "+-", np.std(data[:, -2])/np.sqrt(len(data[:, -2])))
print("(1.5 after nph) Temperature is", np.mean(data[:, 1]), "+-", np.std(data[:, 1])/np.sqrt(len(data[:, 1])))
