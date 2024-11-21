import matplotlib.pyplot as plt
import math as m

t = [i*5 for i in range(16)]
v = [0.02, 0.89, 1.68, 2.37, 2.98, 3.59, 4.04, 4.47, 4.86, 5.19, 5.49, 5.76, 6, 6.21, 6.40, 6.56]

def x(t):
    return 10 - 9.98*m.e**(-0.01*t)

teoretisk = [x(i*5) for i in range(16)]

plt.plot(t,v, label="Målt data")
plt.plot(t, teoretisk, label="teoretisk data")
plt.xlabel("t/s")
plt.ylabel("Vc/v")
plt.legend()
plt.show()


