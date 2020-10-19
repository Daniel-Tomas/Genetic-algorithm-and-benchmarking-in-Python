from group14 import AbstractClasses
import random
import numpy as np

from group14.Genome import Genome


class UniformSelectionOperator(AbstractClasses.SelectionOperator):

    # TODO: Correcion en el maximo y minimo de los genomas al realizar las operaciones, poner nombres bien en ingles

    def apply(self, target, population):

        donors = [target]

        for _ in range(3):
            genome = random.choice(population.collection)
            while genome in donors:
                genome = random.choice(population.collection)
            donors.append(genome)

        donors.remove(target)
        return donors


class Rand1MutationOperator(AbstractClasses.MutationOperator):
    def apply(self, minfun, donors, bounds):
        F = 0.5
        mutantArray = []
        i = 0
        for i in range(len(bounds)):
            min = bounds[i][0]
            max = bounds[i][1]
            subtract_res = donors[1].array[i] - donors[2].array[i]
            multiplication_res = F * subtract_res
            addition_res = donors[0].array[i] + multiplication_res
            if (addition_res < min):
                addition_res = min
            elif (addition_res > max):
                addition_res = max

            mutantArray = np.append(mutantArray, addition_res)
        return Genome(array=mutantArray, fitness=minfun(mutantArray))


class ExponentialCrossoverOperator(AbstractClasses.CrossoverOperator):
    def apply(self, minfun, target, mutant):
        CR = 0.5
        size = len(target.array)
        j = random.randint(0, size - 1)
        candidate = Genome(array=target.array)

        candidate.array[j] = mutant.array[j]
        j = (j + 1) % size
        i = 1
        while i < size and random.random() < CR:
            candidate.array[j] = mutant.array[j]
            j = (j + 1) % size
            i = i + 1

        return Genome(array=candidate.array, fitness=minfun(candidate.array))


class ElitistReplacementOperator(AbstractClasses.ReplacementOperator):
    def apply(self, population, target, candidate):
        if candidate.fitness > target.fitness:
            population.replace(target, candidate)
