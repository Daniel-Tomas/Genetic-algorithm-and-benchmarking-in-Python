from group14 import AbstractClasses
import random
import numpy as np

from group14.Genome import Genome

"""Basic class

    It includes the different operators corresponding to the differential evolution algorithm.

"""

class UniformSelectionOperator(AbstractClasses.SelectionOperator):
    # TODO: Correcion en el maximo y minimo de los genomas al realizar las operaciones, poner nombres bien en ingles

    def apply(self, target, population):
        """Select three random genomes of population different from each other and from the target.

        Args:
            target (Genome): Genome class object selected.
            population (Population): Object which contains a list of genomes.

        Returns:
            donors (array) : contains three different genomes.
        """

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
        """It generate a new genome by combining 'donors'.

        Args:
            minfun (function): Function used to calculate the fitness of a genome.
            donors (array): It contains three different genomes.
            bounds (list): It contains the minimum and maximum values that each variable can take from a candidate
            solution.

        Returns:
            Genome (Genome) : Returns the genome resulting from the combination of the three genomes passed as a
            parameter in the 'donors' array.
        """
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
        """It returns a new candidate by mixing 'target' and 'mutant'.

        Args:
            minfun (function): Function used to calculate the fitness of a genome.
            target (Genome): Genome class object selected.
            mutant (Genome): The genome which we are going to combine with 'target'.

        Returns:
            Genome (Genome) : It is the genome resulting from the combination between 'target' and 'mutant'.
        """
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
        """It include in 'population' the genome with the best fitness between 'target' and 'candidate'

        Args:
            population (Population): Function used to calculate the fitness of a genome.
            target (Genome): Genome class object selected.
            candidate (Genome): Candidate to have better fitness than our 'target' genome.
        """
        if candidate.fitness < target.fitness:
            population.replace(target, candidate)
