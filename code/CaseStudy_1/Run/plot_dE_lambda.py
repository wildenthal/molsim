import matplotlib.pyplot as     plt
import numpy             as     np
from   matplotlib        import colormaps
from   matplotlib.cm     import ScalarMappable

f = lambda x,a,b,c,d: a * x ** 3 + b * x ** 2 + c * x + d
lambdas = np.linspace(0,1,101)

cmap = colormaps['winter_r']

plt.axhline(0, ls='--', c='black', lw=0.5)

data = np.loadtxt("fit_func_params.dat")
for i, line in enumerate(data):
    plt.plot(lambdas, f(lambdas, line[1], line[2], line[3], line[4]), color=cmap(line[0]), label=fr"$\rho =$ {line[0]}")


clb = plt.colorbar(ScalarMappable(cmap=cmap),ax=plt.gca())
clb.ax.set_xlabel(r'$\rho$',labelpad=18,fontsize=10)


plt.xlim((0,1))
plt.xlabel(r"$\lambda$")
plt.ylabel(r"$dE$")
plt.title(r"Fitted 3rd degree polynomial for different values of $\rho$")
# plt.legend()

plt.savefig("dE_lambda_rhos.jpg", dpi=300,bbox_inches='tight',pad_inches=0.1)