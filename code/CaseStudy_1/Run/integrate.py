import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.integrate import simpson
import sys

rho = float(sys.argv[1])
npart = float(sys.argv[2])
lambdanr = float(sys.argv[3])
dx = 1/lambdanr
filename1 = f"data/full_lambda_rho_run/{str(sys.argv[4])}"
filename2 = f"data/full_lambda_rho_run/{str(sys.argv[5])}"


data = np.loadtxt(filename1)
pressures = np.loadtxt(filename2)[:,0]
pid, plj = [pressures[i] for i in (0,-1)]

def func(x, a, b, c, d):
	return a * x ** 3 + b * x ** 2 + c * x + d


popt, pcov = curve_fit(func, data[1:,0], data[1:,1], sigma = np.sqrt(data[1:,2]),absolute_sigma=True)

with open("fit_func_params.dat", "a+") as fit_func_params:
	fit_func_params.write(f"{rho} ")
	for pop in popt:
		fit_func_params.write(f"{pop} ")
	fit_func_params.write("\n")

# def funcval(x):
# 	return func(x,*popt)

# integral, error = quad(funcval,0,1)

# #integral = simpson(data[:,1],dx=dx)

# mu = integral/npart + (plj-pid)/rho

# mu_rho = open("mu_rho_integrated.dat", "a+")
# mu_rho.write(f"{rho} {mu} \n")
# mu_rho.close()

# ### PLOTTING ###

# default = plt.rcParams['lines.markersize']**2
# plt.plot(data[:,0], func(data[:,0],*popt), color='k')
# plt.scatter(data[1:,0],data[1:,1], s=0.3*default)
# #plt.fill_between(data[:,0],func(data[:,0],*(popt+np.sqrt(np.diag(pcov)))),func(data[:,0],*(popt-np.sqrt(np.diag(pcov)))),alpha=0.3,color='orange')
# plt.fill_between(data[:,0],data[:,1]-np.sqrt(data[:,2]),data[:,1]+np.sqrt(data[:,2]),alpha=0.3,color='pink')
# plt.plot([],[],'',label="Integral: {} +- {}".format(integral,error))
# plt.legend()
# plt.ylim([-300,300])
# plt.savefig(f'integral{rho}.jpg',dpi=300)
# #print(popt,'\n', np.sqrt(np.diag(pcov)))
# #plt.figure()
# #plt.yscale('log')
# #plt.plot(data[:,0],np.sqrt(data[:,2]))
# #plt.savefig('standard_deviation_dEdl.jpg',dpi=300)
