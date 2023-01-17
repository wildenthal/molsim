import matplotlib.pyplot as     plt
import numpy             as     np
from   matplotlib        import colormaps
from   matplotlib.cm     import ScalarMappable

u = lambda r,l: 4*(l**5*r**-12 - l**3*r**-6)
x = np.arange(.99,2,.01)
l = np.arange(0,1,0.09)

cmap = colormaps['winter_r']

fig = plt.figure()
for l in l:
    plt.plot(x,u(x,l),color=cmap(l))
plt.xlabel(r'${r}\: /\: {\sigma}$',fontsize = 10)#, fontsize = 20)
plt.ylabel(r'$V_{LJ}\: /\: \epsilon$',fontsize=10)
clb = plt.colorbar(ScalarMappable(cmap=cmap),ax=plt.gca())
clb.ax.set_xlabel(r'$\lambda$',labelpad=18,fontsize=10)
plt.title('Modified Lennard-Jones Potential')
plt.savefig('modLJ.jpg',dpi=300,bbox_inches='tight',pad_inches=0.1)
