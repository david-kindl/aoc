from solution import Solution


class Solve(Solution):
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.patterns = self.__parse()

    @property
    def part_1(self) -> int:
        return self.__get_mirror_score(0)

    @property
    def part_2(self) -> any:
        return self.__get_mirror_score(1)

    def __parse(self):
        patterns = []
        curr_pattern = []
        with open(self.file_name, 'r') as fl:
            for line in fl.readlines():
                line = line.rstrip('\n')
                if 0 < len(line):
                    curr_pattern.append(line)
                else:
                    if 0 < len(curr_pattern):
                        patterns.append(curr_pattern)
                        curr_pattern = []
        if 0 < len(curr_pattern):
            patterns.append(curr_pattern)
        return patterns

    def __get_mirror_score(self, num_diff: int) -> int:
        col_idx = 0
        row_idx = 0
        for pattern in self.patterns:
            col_idx += 100 * self.__get_simple_mirror_idx(pattern, num_diff)
            row_idx += self.__get_simple_mirror_idx(self.__transpose(pattern), num_diff)
        return col_idx + row_idx

    @staticmethod
    def __transpose(pattern: list[str]) -> list[str]:
        return [''.join(p) for p in zip(*pattern)]

    @staticmethod
    def __get_simple_mirror_idx(pattern: list[str], num_diff: int) -> int:
        start = 0
        end = len(pattern)
        for i in range(1, end):
            rng = min(abs(i - start), abs(i - end))
            a = [ord(char) for item in pattern[i - rng: i] for char in item]
            b = [ord(char) for item in pattern[i: i + rng][::-1] for char in item]
            diff = 0
            for j in range(len(a)):
                diff += abs(a[j] - b[j])
            if diff / 11 == num_diff:  # Abs difference between a dot and a hash mark is 11.
                return i
        return 0
