import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('lambda.dat')
data[:,2] = np.sqrt(data[:,2])

plt.fill_between(data[:,0],data[:,1]+data[:,2],data[:,1]-data[:,2], alpha=0.3)
plt.scatter(data[:,0],data[:,1])
plt.ylim([-250,250])
plt.savefig('areas.jpg',dpi=300)

