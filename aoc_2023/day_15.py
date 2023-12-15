from solution import Solution


class Solve(Solution):
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.sequences = self.__parse()

    @property
    def part_1(self) -> any:
        scores = [self.__build_hash(val) for val in self.sequences]
        return sum(scores)

    @property
    def part_2 (self) -> any:
        pass

    def __parse(self):
        with open(self.file_name, 'r') as fl:
            sequence = [val for seq in fl.readlines() for val in seq.strip('\n').split(',')]
        return sequence

    @staticmethod
    def __build_hash(string: str) -> int:
        curr_value = 0
        for char in string:
            curr_value += ord(char)
            curr_value *= 17
            curr_value %= 256
        return curr_value


if __name__ == '__main__':
    s = Solve('/home/david/repo/aoc/cache/2023/day_15.txt')
    print(s.part_1)
