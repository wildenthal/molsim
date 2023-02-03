import numpy as np
import matplotlib.pyplot as plt
from   matplotlib        import colormaps

data_widom = np.loadtxt("data/mu_rho_widom.dat")
data_integral = np.loadtxt("data/mu_rho_integrated.dat")

steps = data_integral[:,0]

plt.axhline(0, ls='--', c='black', lw=0.5)

plt.plot(steps, data_widom[:,1], '-o', label="Widom Method", c=colormaps['winter_r'](0))
plt.plot(steps, data_integral[:,1], '-o', label="Thermodynamic Integration")

plt.xlabel(r"$\rho$")
plt.ylabel(r"$\mu$")
plt.title(r"$\mu$-values for different $\rho$-values calculated" "\n" r"using both Widom and Thermodynamic Integration Methods")

plt.legend()

plt.savefig("mu_rho_comparison.jpg", dpi=300,bbox_inches='tight',pad_inches=0.1)