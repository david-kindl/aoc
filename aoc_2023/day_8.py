from solution import Solution


class Solve(Solution):
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.__get_data()

    @property
    def part_1(self) -> int:
        start = 'AAA'
        finish = 'ZZZ'
        curr_elem = start
        i = 0
        while True:
            if curr_elem == finish:
                return i
            step = self.__get_current_step(i)
            curr_elem = self.map[curr_elem][step]
            i += 1

    @property
    def part_2(self) -> int:
        start_nodes = [node for node in self.map.keys() if node.endswith('A')]
        z_loc = []
        for node in start_nodes:
            curr_elem = node
            i = 0
            while True:
                if curr_elem.endswith('Z'):
                    z_loc.append(i)
                    break
                step = self.__get_current_step(i)
                curr_elem = self.map[curr_elem][step]
                i += 1
        return self.list_lcm(z_loc)

    def __get_data(self) -> None:
        with open(self.file_name, 'r') as fl:
            _map = {}
            steps = self.__get_steps(fl.readline())
            fl.readline()  # skip empty line
            for line in fl.readlines():
                key, val = self.__get_map(line)
                _map[key] = val  # Dictionaries are insertion ordered from python 3.6
        self.steps = steps
        self.map = _map

    @staticmethod
    def __get_steps(line: str) -> tuple[int, ...]:
        return tuple(int(char == 'R') for char in line.strip('\n'))

    @staticmethod
    def __get_map(line: str) -> tuple[str, list[str]]:
        line = line.translate({ord('('): ' ', ord(')'): ' ', ord('\n'): ' '}).replace(' ', '')
        key, val = line.split('=')
        val = val.split(',')
        return key, val

    def __get_current_step(self, i: int) -> int:
        return self.steps[int((i % len(self.steps)))]

    @staticmethod
    def list_lcm(loc: list[int]) -> int:
        def gcd(a: int, b: int) -> int:
            if a == 0:
                return b
            return gcd(b % a, a)

        def lcm(a: int, b: int) -> int:
            return (a // gcd(a, b)) * b

        while 1 < len(loc):
            loc = sorted([val for val in set(loc)])
            _lcm = lcm(loc[0], loc[1])
            del loc[0:2]
            loc.append(_lcm)

        return loc[0]
