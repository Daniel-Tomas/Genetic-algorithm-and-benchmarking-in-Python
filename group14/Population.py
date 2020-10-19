from group14.Genome import Genome


class Population:
    """Basic class

        It creates a collection of Genomes.

        Atributes:
                Genome (array): Genome class object
        """

    def __init__(self, minfun, bounds, psize):
        self.collection = []
        for _ in range(0, psize):
            self.add(Genome(minfun=minfun, bounds=bounds))

    def __repr__(self):
        """
        It casts the Population elements in String format.

        Returns:
             str: The population in string format
        """
        res = '[ '
        for elem in self.collection:
            res += f'[ {elem.array}, fitness={elem.fitness} ], '
        return res

    def ascendent_sort(self):
        """It sort Genomes of 'self' by fitness in ascending order.
        """
        self.collection.sort(key=lambda x: x.fitness)

    def descendent_sort(self):
        """It sort Genomes of 'self' by fitness in descending order.
        """
        self.collection.sort(key=lambda x: x.fitness, reverse=True)

    def add(self, genome):
        """Add an element of type Genome to the end of 'self'
        Args:
            genome(array): Genome class object
        """
        self.collection.append(genome)

    def remove(self, genome):
        """Remove the genome passed as an argument to 'self'.
        Excepcion en caso de que no esté el elemento a elminar

        Args:
            genome(array): Genome class object
        """
        # for elem in self.collection:
        #     if elem == genome:
        self.collection.remove(genome)

    def replace(self, genomerm, genomerp):
        """Replace genomerm with genomerp in the 'self' array
        Excepcion en caso de que no esté el elemento a elminar

        Args:
            genomerm(array): Genome class object
            genomerp(array): Genome class object
        """
        # for elem in self.collection:
        #     if elem == genome:
        self.remove(genomerm)
        self.add(genomerp)

# genome1 = Genome([1, 33, 4], 3)
# genome2 = Genome([1, 33, 5], 4)
# genome3 = Genome([2, 33, 4], 1)
#
# genome4 = Genome([2, 33, 4], -1)
#
# prueba = Population([genome1, genome2, genome3])
# prueba.ascendent_sort()
#
# prueba.add(genome4)
# print(prueba)
#
# prueba.remove(genome2)
# print(prueba)

# def f(sol):
#     return sum(sol)
#
#
# prueba = Population(f, [(0, 1), (0, 1)], 3)
# print(prueba)
