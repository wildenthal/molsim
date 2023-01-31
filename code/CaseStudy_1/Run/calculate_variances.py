import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt("lj.prt")
steps = data[:,0]
labels = ['simulation step', 'energy', 'pressure', ' dE/dlambda ']



for i in [1,2,3]:
	values = data[:,i]
	mean = values.mean()
	relvar = values.std()/mean
	print("Column {}: Average value {} with relative variance {}".format(i,mean,values.std()/mean))
	plt.figure()
	plt.plot(steps,values)
	plt.xlabel(labels[0])
	plt.ylabel(labels[i])
	plt.savefig("data/figure{}.jpg".format(i), dpi=300)
	plt.figure()
	plt.hist(values)
	plt.xlabel(labels[0])
	plt.ylabel(labels[i])
	plt.title(r"Value {:.2f} (1 +- {:.2f})".format(mean,relvar))
	plt.savefig("data/histogram{}.jpg".format(i),dpi=300)
