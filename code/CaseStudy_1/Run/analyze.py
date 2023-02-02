import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("mu.dat")

steps = data[:,0]

for i in [1]:
	values = data[:,i]
	# mean = values.mean()
	# print("Column {}: Average value {} with relative variance {}".format(i,mean,values.std()/mean))
	plt.figure()
	plt.plot(steps,values)
	plt.xlabel(r"$\rho$")
	plt.ylabel(r"$\mu_{ex}$")
	plt.axhline(0,ls='--')
	plt.savefig("data/mu_rho.jpg", dpi=300)


