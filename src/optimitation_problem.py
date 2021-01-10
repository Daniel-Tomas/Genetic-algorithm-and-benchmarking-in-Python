from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import numpy as np

from EA import EA
from Data import *


def f(array):
    return our_fitness(array)


def our_fitness(array):
    res = 0
    for i in range(len(array)):
        mark = (array[i] * point_per_hour[i])
        if student_luck[i] <= revision_probability[i]:
            mark += revision_mark[i]
        if mark > 10:
            mark = 10
        res += mark * credits[i]
    nota = res / sum(credits)
    if sum(array) > study_hours:
        return -((sum(array) - study_hours) ** 2 / nota)
    return nota


min_hour = [int(b) / int(m) for b, m in zip(minimum_marks, point_per_hour)]
mybounds = [(minimum_marks[i] / point_per_hour[i], 10 / point_per_hour[i]) for i in range(len(credits))]

population_size = int(input('Introduzca el tamaño de población, en caso de no hacerlo y pulsar'
                            ' la tecla "enter" el valor será "50": ') or '50')

myEA = EA(f, mybounds, population_size)

iterations = int(input('Introduzca el número de iteraciones, en caso de no hacerlo y pulsar'
                       ' la tecla "enter" el valor será "500": ') or '500')

print(f'El número de asignaturas a evaluar son: {len(minimum_marks)}')

np.set_printoptions(precision=3)
print(f'Las horas mínimas de estudio por cada asignatura son: \n'
      f'Horas mínimas: {np.array(min_hour)}')

myEA.run(iterations)

print(f'Best Genome: {myEA.best()}')
print(f'Según el algoritmo, obtendría la mejor nota estudiando un total de: {sum(myEA.best_genome.array):.5} '
      f'horas \n')

print(f'----------------------------- \n')

print(f'Ahora vamos a ajecutar el algoritmos varias veces para ver como se comporta con un tamaño de población = 50'
      f' y 500 iteraciones')

reps = int(input('Por favor, introduce el número de repeticiones que desea ejecutar el algoritmo: ') or '10')

best_fitness = []
worst_fitness = []
values_myEA = []
for i in range(reps):
    values = []
    myEA = EA(f, mybounds, 50)
    myEA.run(500)
    print(f'Best Genome: {myEA.best()}')
    best_fitness.append(myEA.best_genome.fitness)
    for i in myEA.population.collection:
        values.append(i.fitness)
    values_myEA.append(values)

fig1, ax1 = plt.subplots()
ax1.set_title("Best fitness of each repetition", fontsize=18)
ax1.boxplot(best_fitness, showmeans=True, meanline=True)
line1 = Line2D([0], [0], color='orange', linewidth=1, linestyle='-')
line2 = Line2D([0], [0], color='green', linewidth=1, linestyle='--')
lines = [line1, line2]
labels = ['mean', 'median']
plt.legend(lines, labels, fontsize='large')
# plt.xlabel("Samples")
plt.xticks([])
plt.ylabel("Marks", fontsize=14)
plt.savefig('grafica_1.png')
plt.show()

fig2, ax2 = plt.subplots()
ax2.set_title("Fitness of each repetition", fontsize=18)
ax2.boxplot(values_myEA, showmeans=True, meanline=True)
plt.legend(lines, labels, fontsize='large')
# plt.xlabel("Samples")
plt.ylabel("Marks", fontsize=14)
plt.savefig('grafica_2.png')
plt.show()
