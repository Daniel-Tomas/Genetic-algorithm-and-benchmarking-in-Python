from Genome import Genome


class Population:
    """Basic class

    Creates a collection of Genomes.

    Attributes:
        collection (list): list of genomes.

    Args:
        minfun (function): Function used to calculate the fitness of a genome.
        bounds (list): Contains the minimum and maximum values that each variable can take from a candidate
            solution.
        p_size (int): Maximum size of our population.
    """

    def __init__(self, minfun, bounds, p_size):
        self.collection = []
        for _ in range(p_size):
            self.add(Genome(bounds=bounds, minfun=minfun))

    def __repr__(self):
        """
        Casts the Population elements in String format.

        Returns:
             str: The population in string format.
        """
        res = '{ '
        for index, elem in enumerate(self.collection):
            if index == len(self.collection) - 1:
                res += f'[ {elem.array}, fitness={elem.fitness} ] }}'
            else:
                res += f'[ {elem.array}, fitness={elem.fitness} ], '
        return res

    def ascendent_sort(self):
        """Sort Genomes of 'self' by fitness in ascending order.
        """
        self.collection.sort(key=lambda x: x.fitness)

    def descendent_sort(self):
        """Sort Genomes of 'self' by fitness in descending order.
        """
        self.collection.sort(key=lambda x: x.fitness, reverse=True)

    def add(self, genome):
        """Add an element of type Genome to the end of 'self'.
        Args:
            genome(array): Genome class object to be added to the end of 'self'.
        """
        self.collection.append(genome)

    def remove(self, genome):
        """Remove the genome passed as an argument to 'self'.
        Excepcion en caso de que no esté el elemento a elminar

        Args:
            genome(array): Genome class object that will be removed from 'self'.
        """

        self.collection.remove(genome)

    def replace(self, genomerm, genomerp):
        """Replace genomerm with genomerp in the 'self' array.
            Excepcion en caso de que no esté el elemento a elminar.

        Args:
            genomerm(array): Genome class object that will be removed from 'self'.
            genomerp(array): Genome class object to replace 'genomerm'.
        """
        self.remove(genomerm)
        self.add(genomerp)
