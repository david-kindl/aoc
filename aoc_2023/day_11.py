from solution import Solution


class Solve(Solution):
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    @property
    def part_1(self) -> any:
        return self.__solve(1)

    @property
    def part_2(self) -> any:
        return self.__solve(999999)

    def __solve(self, expansion: int) -> int:
        galaxies = self.__get_galaxies(expansion)
        diff = 0
        cnt = 0
        for i in range(len(galaxies)):
            for j in range(i + 1, len(galaxies)):
                a, b = galaxies[i], galaxies[j]
                diff += (max(a[0], b[0]) - min(a[0], b[0])) + (max(a[1], b[1]) - min(a[1], b[1]))
        return diff

    def __get_galaxies(self, expansion: int) -> list[tuple[int, int]]:
        with open(self.file_name, 'r') as fl:
            universe = [line.rstrip() for line in fl.readlines()]
        y_mod = self.__expand(universe, expansion)
        # Translating the list to evaluate expand logic the same way
        x_mod = self.__expand([''.join(obj) for obj in zip(*universe)], expansion)

        galaxies = []
        for y, line in enumerate(universe):
            for x, obj in enumerate(line):
                if obj == '#':
                    galaxies.append((y_mod[y], x_mod[x]))
        return galaxies

    @staticmethod
    def __expand(galaxy_map: list[str], expansion: int) -> dict[int, int]:
        idx_map = {}
        modifier = 0
        for i, line in enumerate(galaxy_map):
            idx_map[i] = i
            if line == ('.' * len(galaxy_map)):
                modifier += expansion
            idx_map[i] += modifier
        return idx_map
