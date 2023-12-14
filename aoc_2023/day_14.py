from solution import Solution


class Solve(Solution):
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.platform = self.__parse()

    @property
    def part_1(self) -> any:
        n_edge = len(self.platform)
        score = 0
        for i, beam in enumerate(self.platform):
            score += (n_edge - i) * len([rock for rock in beam if rock == 'O'])
        return score

    @property
    def part_2(self) -> any:
        pass

    def __parse(self):
        with open(self.file_name, 'r') as fl:
            platform = [line.rstrip('\n') for line in fl.readlines()]
        platform = self.__tilt_north(platform)
        return platform

    @staticmethod
    def __tilt_north(platform: list[str]) -> list[list[str]]:
        platform = [list(p) for p in zip(*platform)]
        s_edge = len(platform)
        for i in range(s_edge):
            unmovable_rocks = set(i for i, rock in enumerate(platform[i]) if rock == '#')
            unmovable_rocks.add(s_edge - 1)
            s = 0
            for ur in sorted(unmovable_rocks):
                platform[i][s:ur + 1] = sorted(platform[i][s:ur + 1], reverse=True)
                s = ur + 1
        return [list(p) for p in zip(*platform)]


if __name__ == '__main__':
    s = Solve('/home/david/repo/aoc/cache/2023/day_14.txt')
    print(s.part_1)
