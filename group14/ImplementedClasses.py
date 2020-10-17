from group14 import AbstractClasses
import random
from numpy import subtract, array, clip

from group14.Genome import Genome


class UniformSelectionOperator(AbstractClasses.SelectionOperator):

    # TODO: Poner bien los range && pensar cambiar todo a numpy.array
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
        min = bounds[0][0]
        max = bounds[0][1]
        subtract_res = clip((array(donors[1].array) - array(donors[2].array)), min, max)
        multiplication_res = clip(F * subtract_res, min, max)
        addition_res = clip(array(donors[0].array) + multiplication_res, min, max)
        res_array = list(addition_res)
        return Genome(array=res_array, fitness=minfun(res_array))


class ExponentialCrossoverOperator(AbstractClasses.CrossoverOperator):
    def apply(self, minfun, target, mutant):
        CR = 0.5
        size = len(target.array)
        j = random.randint(0, size - 1)
        candidate = Genome(array=target.array)
        candidate.array[j] = mutant.array[j]
        j = (j + 1) % size
        i = 1
        while i < size - 1 and random.random() >= CR:
            candidate.array[j] = mutant.array[j]
            j = (j + 1) % size
            i = i + 1

        return Genome(array=candidate.array, fitness=minfun(candidate.array))


class ElitistReplacementOperator(AbstractClasses.ReplacementOperator):
    def apply(self, population, target, candidate):
        if candidate.fitness > target.fitness:
            population.replace(target, candidate)
