import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from scipy.integrate import quad

data = np.loadtxt('lambda.dat')
def func(x, a, b, c, d):
	return a * x ** 3 + b * x ** 2 + c * x + d


popt, pcov = curve_fit(func, data[:,0], data[:,1], sigma = np.sqrt(data[:,2]),absolute_sigma=True)

default = plt.rcParams['lines.markersize']**2

plt.plot(data[:,0], func(data[:,0],*popt), color='k')
plt.scatter(data[:,0],data[:,1], s=0.3*default)
plt.fill_between(data[:,0],func(data[:,0],*(popt+np.sqrt(np.diag(pcov)))),func(data[:,0],*(popt-np.sqrt(np.diag(pcov)))),alpha=0.3,color='orange')
plt.fill_between(data[:,0],data[:,1]-np.sqrt(data[:,2]),data[:,1]+np.sqrt(data[:,2]),alpha=0.3,color='pink')

def funcval(x):
	return func(x,*popt)

integral, error = quad(funcval,0,1)

plt.plot([],[],'',label="Integral: {} +- {}".format(integral,error))
plt.legend()

plt.ylim([-300,300])

plt.savefig('integral.jpg',dpi=300)

print(popt,'\n', np.sqrt(np.diag(pcov)))
plt.figure()

plt.yscale('log')
plt.plot(data[:,0],np.sqrt(data[:,2]))

plt.savefig('standard_deviation_dEdl.jpg',dpi=300)
