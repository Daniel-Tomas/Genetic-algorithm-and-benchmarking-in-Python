# import numpy as np
#
# np.set_printoptions(linewidth=np.inf)
# # np.random.seed(5)
# with open("numbers.out", 'w') as f:
#     for _ in range(1):
#         array = np.random.randint(0, 30000, (1, 1000))
#         f.write('1000 ')
#         for n in array:
#             f.write(f'{n}')
#         f.write('\n')


import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# plt.style.use('dark_background')
plt.rcParams.update({
    "lines.color": "white",
    "patch.edgecolor": "white",
    "text.color": "white",
    "axes.facecolor": "#121111",
    "axes.edgecolor": "lightgray",
    "axes.labelcolor": "white",
    "xtick.color": "white",
    "ytick.color": "white",
    "grid.color": "lightgray",
    "figure.facecolor": "#121111",
    "figure.edgecolor": "black",
    "savefig.facecolor": "#121111",
    "savefig.edgecolor": "black"})

n = np.linspace(0.1, 10000, 10000)
# Generamos una grafica lineal para una recta en X
# Generamos otra grafica lineal para una X cuadratica
# Generamos una grafica lineas para una X Cubica
plt.plot(n, n ** 2, label='$\mathcal{O}(n^2)$ - Brute Force')

plt.plot(n, 0.5 * (n ** 2), label='$\mathcal{O}(0,5n^2)$ - Probabilistic')

plt.plot(n, n + 10 * n, label='$\mathcal{O}(5(n+n)$ - Radix Sort')

plt.plot(n, np.log2(n) * n, label='$\mathcal{O}(n \log n)$ - Quick Sort')

plt.plot(n, n, label='$\mathcal{O}(n)$')

# plt.plot(n, np.log(n), label='$\mathcal{O}(log n)$')

plt.xlim(0, 1000)
plt.ylim(0, 15000)
# plt.yticks(np.arange(0, 15000,1500))


# Agregamos las etiquetas y añadimos una leyenda.
plt.xlabel('Size of input (n)', fontsize=16)
plt.ylabel('Iterations', fontsize=16)
# plt.xlabel('Eje X')
# plt.ylabel('Eje Y')
# plt.title("Complexity")
plt.legend(fontsize='large', framealpha=0.6)
plt.savefig('grafica_lineal.png')
plt.show()

# x = np.linspace(0.001, 2, 100)
# #Generamos una grafica lineal para una recta en X
# plt.plot(x, x, label='linear')
# #Generamos otra grafica lineal para una X cuadratica
# plt.plot(x, x**2, label='quadratic')
# #Generamos una grafica lineas para una X Cubica
# plt.plot(x, x**3, label='cubic')
# #Agregamos las etiquetas y añadimos una leyenda.
# plt.xlabel('Eje X')
# plt.ylabel('Eje Y')
# plt.title("Simple Plot")
# plt.legend()
# plt.savefig('grafica_lineal.png')
# plt.show()
