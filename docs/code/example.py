import collections.abc as abs


class Cubes:
    def __init__(self, limit):
        self.limit = limit
        self.n = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n >= self.limit:
            raise StopIteration
        result = self.n**3
        self.n += 1
        return result

    def __repr__(self) -> str:
        return f"Cubes({self.limit})"


def get_cube(cube: abs.Iterable):
    for i in cube:
        return i**3


cube = Cubes(10)

get_cube([1, 2, 3, 4, 5])
get_cube(cube)

get_cube(1)  
#  Argument of type "Literal[1]" cannot be assigned to parameter "cube" of type "Iterable[Unknown]" in function "get_cube"
#  "Literal[1]" is incompatible with protocol "Iterable[Unknown]"
#  "__iter__" is not presentPylancereportGeneralTypeIssues