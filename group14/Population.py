from group14.Genome import Genome


class Population:
    """Basic class

    It creates a collection of Genomes.

    Atributes:
            Genome (array): Genome class object
    """

    def __init__(self, minfun, bounds, psize):
        self.collection = []
        for _ in range(psize):
            self.add(Genome(bounds=bounds, minfun=minfun))

    def __repr__(self):
        """
        It casts the Population elements in String format.

        Returns:
             str: The population in string format
        """
        res = '{ '
        for index, elem in enumerate(self.collection):
            if index == len(self.collection) - 1:
                res += f'[ {elem.array}, fitness={elem.fitness} ] }}'
            else:
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
        self.remove(genomerm)
        self.add(genomerp)


# def f(sol):
#     return sum(sol)
#
#
# prueba = Population(f, [(0, 1), (0, 1)], 3)
# print(prueba)
#
# # genome1 = Genome(array=[1, 33, 4],fitness= 3)
# # genome2 = Genome(array=[1, 33, 5], fitness=4)
# # genome3 = Genome(array=[2, 33, 4], fitness=1)
#
# genome4 = Genome(array=[2, 33, 4], fitness=-1)
#
# prueba.ascendent_sort()
# print(prueba)
#
# prueba.add(genome4)
# print(prueba)
#
# prueba.remove(genome4)
# print(prueba)
#
# print(len(prueba.collection[0].array))
