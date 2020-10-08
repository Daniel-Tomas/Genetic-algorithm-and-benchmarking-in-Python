from abc import ABC, abstractmethod


class CrossoverOperator(ABC):
    @abstractmethod
    def apply(self, collection):
        """
        Args:
            collection:
        """
        ...


class MutationOperator(ABC):
    @abstractmethod
    def apply(self, collection):
        """
        Args:
            collection:
        """
        ...


class SelectionOperator(ABC):
    @abstractmethod
    def apply(self, collection):
        """
        Args:
            collection:
        """
        ...


class ReplacementOperator(ABC):
    @abstractmethod
    def apply(self, collection1, collection2):
        """
        Args:
            collection1:
            collection2:
        """
        ...
