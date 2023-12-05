from solution import Solution


class Solve(Solution):
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.locations = self.__get_data()

    @property
    def part_1(self) -> any:
        pass

    @property
    def part_2(self):
        pass

    def __get_data(self):
        locations = {}
        with open(self.file_name) as fl:
            for line in fl.readlines():
                if len(line) > 1:
                    if line.find(':') > -1:
                        key, content = line.split(':')
                        locations.setdefault(key, [])
                        if len(content) > 1:
                            locations[key] = [tuple(int(val) for val in content.split())]
                    else:
                        locations[key].append(tuple(int(val) for val in line.split()))
        return locations


if __name__ == '__main__':
    solution = Solve('/home/david/repo/aoc/cache/2023/day_5.txt')
    print(solution.locations)
