import numpy as np
import scipy
import matplotlib.pyplot as plt

fig, ax1 = plt.subplots()
k=np.array([11,23,43,61,81])
t=np.array([1.34,7.37,89.78,404.76,1433.87])
ax1.set_xlabel('S')
ax1.set_ylabel('t')
ax1.plot(k,t)
plt.title('le temps de recherche en fonction de S')

fig, ax2 = plt.subplots()
k=np.array([2,3,4,5,6])
t=np.array([0,0.0001,89.78,450.83,3568.63])
ax2.set_xlabel('k')
ax2.set_ylabel('t')
ax2.plot(k,t)
plt.title('le temps de recherche en fonction de k')

fig, ax3 = plt.subplots()
k=np.array([i for i in range(1,51)])
t=np.array(list(map(int,"3259570 53049 3396043 1585509 813804 3746913 4169006 3048767 3183951 3845941 779748 2270340 2365427 2297233 5127053 5034367 3383169 3366524 4651125 3377293 2869863 2927298 5177132 2365084 5132273 4527117 4137991 4026898 729469 3321292 1285254 1999642 3960928 2139212 4044551 2949744 4667547 773458 738375 5151381 364301 1335246 3429626 3841922 1595686 2898984 5078067 1932814 5158504 1502272".split())))
ax3.scatter(k,t)
plt.title('le polynome de cryptage p-modulaire')
plt.grid()
plt.show()
