from group14 import AbstractClasses
import random
from numpy import subtract, array

from group14.Genome import Genome


class UniformSelectionOperator(AbstractClasses.SelectionOperator):

    # TODO: Poner bien los range y cambiar argumentos de clases abstractas | pensar cambiar todo a numpy.array
    # TODO: Poner argumentos opcionales al genoma preguntar sobre las funciones que nos pasan a minimizar
    # TODO: Correcion en el maximo y minimo de los genomas al realizar las operaciones

    def apply(self, target, population):

        donors = [target]

        for _ in range(3):
            genome = random.choice(population)
            while genome in donors:
                genome = random.choice(population)
            donors.append(genome)

        donors.remove(target)
        return donors


class Rand1MutationOperator(AbstractClasses.MutationOperator):
    def apply(self, minfun, donors):
        F = 0.5

        res_array = list(array(donors[0].array) + F * (array(donors[1].array) - array(donors[2].array)))
        return Genome(res_array, minfun(res_array))


class ExponentialCrossoverOperator(AbstractClasses.CrossoverOperator):
    def apply(self, minfun, target, mutant):
        CR = 0.5
        size = len(target.array)
        j = random.randint(0, size - 1)
        candidate = Genome(target.array)
        candidate.array[j] = mutant.array[j]
        j = (j + 1) % size
        i = 1
        while i < size - 1 and random.random() >= CR:
            candidate.array[j] = mutant.array[j]
            j = (j + 1) % size
            i = i + 1

        return Genome(candidate.array, minfun(candidate.array))


class ElitistReplacementOperator(AbstractClasses.ReplacementOperator):
    def apply(self, population, target, candidate):
        if candidate.fitness > target.fitness:
            population.replace(target, candidate)
