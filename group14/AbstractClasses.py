from abc import ABC, abstractmethod


class SelectionOperator(ABC):
    @abstractmethod
    def apply(self, minfun, target, mutant):
        """
        Args:
            collection:
        """
        ...


class MutationOperator(ABC):
    @abstractmethod
    def apply(self, minfun, donors, bounds):
        """
        Args:
            collection:
        """
        ...


class CrossoverOperator(ABC):
    @abstractmethod
    def apply(self, target, population):
        """
        Args:
            collection:
        """
        ...


class ReplacementOperator(ABC):
    @abstractmethod
    def apply(self, population, target, candidate):
        """
        Args:
            collection1:
            collection2:
        """
        ...
