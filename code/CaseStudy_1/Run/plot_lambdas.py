import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("lambda.dat")

lambdas = data[:,0]

for i in [1]:
	values = data[:,i]
	plt.figure()
	plt.plot(lambdas,values)
	plt.savefig("data/lambdas.jpg".format(i), dpi=300)
