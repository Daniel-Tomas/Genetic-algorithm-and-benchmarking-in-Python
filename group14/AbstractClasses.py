from abc import ABC, abstractmethod


class SelectionOperator(ABC):
    @abstractmethod
    def apply(self, target, population):
        """
        Args:
            target (Genome): Genome class object selected.
            population (Population): Object which contains a list of genomes.
        """
        ...


class MutationOperator(ABC):
    @abstractmethod
    def apply(self, donors, bounds):
        """
        Args:
            minfun (function): Function used to calculate the fitness of a genome.
            donors (array): It contains three different genomes.
            bounds (list): It contains the minimum and maximum values that each variable can take from a candidate
            solution.
        """
        ...


class CrossoverOperator(ABC):
    @abstractmethod
    def apply(self, target, mutant):
        """
        Args:
            minfun (function): Function used to calculate the fitness of a genome.
            target (Genome): Genome class object selected.
            mutant (Genome): The genome which we are going to combine with 'target'.
        """
        ...


class ReplacementOperator(ABC):
    @abstractmethod
    def apply(self, population, target, candidate):
        """
        Args:
            population (Population): Function used to calculate the fitness of a genome.
            target (Genome): Genome class object selected.
            candidate (Genome): Candidate to have better fitness than our 'target' genome.
        """
        ...
