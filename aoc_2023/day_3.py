from solution import Solution


class Solve(Solution):
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.raw_content = self.__get_raw_data()
        self.numbers, self.symbols = self.__parse()
        self.__pt1, self.__pt2 = self.__evaluate()

    @property
    def part_1(self) -> int:
        return self.__pt1

    @property
    def part_2(self) -> int:
        return self.__pt2

    def __get_raw_data(self):
        with open(self.file_name, 'r') as fl:
            content = fl.readlines()
        return content

    def __parse(self):
        numbers = {}
        symbols = {}
        for i, line in enumerate(self.raw_content):
            curr_num = ''
            idx_list = []
            for j, char in enumerate(line):
                if char.isdigit():
                    curr_num += char
                    idx_list.append(j)
                else:
                    if char not in ('.', '\n'):
                        symbols.setdefault(char, [])
                        symbols[char].append((i, j))
                    if len(curr_num) > 0:
                        coord = [(i, x) for x in idx_list]
                        for c in coord:
                            numbers[c] = int(curr_num)
                        curr_num = ''
                        idx_list = []
        return numbers, symbols

    def __evaluate(self) -> tuple[int, int]:
        engine_parts = 0
        gear_ratio = 0
        for sym, locations in self.symbols.items():
            for loc in locations:
                neighbours = self.__get_neighbours(loc)
                engine_parts += sum(neighbours)
                if sym == '*' and len(neighbours) == 2:
                    gear_ratio += neighbours[0] * neighbours[1]
        print(engine_parts, gear_ratio)
        return engine_parts, gear_ratio

    def __get_neighbours(self, loc: tuple[int, int]) -> list[int]:
        y, x = loc
        dim = len(self.raw_content)
        neighbours = set()
        y_min = max(y - 1, 0)
        y_max = min(y + 1, dim) + 1
        x_min = max(x - 1, 0)
        x_max = min(x + 1, dim) + 1
        for i in range(y_min, y_max):
            for j in range(x_min, x_max):
                try:
                    neighbours.add((i, self.numbers[(i, j)]))
                except KeyError:
                    pass
        return [n[1] for n in neighbours]
