import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("lj.prt")

steps = data[:,0]

for i in [1,2,3]:
	values = data[:,i]
	mean = values.mean()
	print("Column {}: Average value {} with relative variance {}".format(i,mean,values.std()/mean))
	plt.figure()
	plt.plot(steps,values)
	plt.savefig("data/figure{}.jpg".format(i), dpi=300)
