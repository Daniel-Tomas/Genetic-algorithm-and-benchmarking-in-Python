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
    def apply(self, target, population):
        """
         Args:
            target (Genome): Genome class object selected.
            population (Population): Object which contains a list of genomes.
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
