from solution import Solution


class Solve(Solution):
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.springs = []
        self.config = []
        self.__get_condition_records()
        self.cache = {}

    @property
    def part_1(self) -> int:
        variations = 0
        for i in range(len(self.springs)):
            variations += self.__get_variations(self.springs[i], self.config[i])
        return variations

    @property
    def part_2(self) -> int:
        variations = 0
        for i in range(len(self.springs)):
            spring = '?'.join([self.springs[i]] * 5)
            config = self.config[i] * 5
            variations += self.__get_variations(spring, config)
        return variations

    def __get_condition_records(self) -> None:
        with open(self.file_name, 'r') as fl:
            for line in fl.readlines():
                line = line.rstrip('\n')
                springs, config = line.split(' ')
                config = tuple(map(int, config.split(',')))
                self.springs.append(springs)
                self.config.append(config)

    def __get_variations(self, springs: str, config: tuple[int, ...]):
        # Couldn't do it myself, so I studied and reworked this solution:
        # https://www.youtube.com/watch?v=g3Ms5e7Jdqo
        # Base cases:
        #   no more springs are left and no more configurable elements are left (final case)
        if springs == '':
            return 1 if config == () else 0
        #   no more configurations are left and no more damaged springs are left
        if config == ():
            return 1 if '#' not in springs else 0

        # Caching:
        key = (springs, config)
        if key in self.cache:
            return self.cache[key]

        variations = 0

        if springs[0] in '.?':
            variations += self.__get_variations(springs[1:], config)

        if springs[0] in '#?':
            if (
                config[0] <= len(springs)                                       # It's possible to find a match
                and '.' not in springs[:config[0]]                              # There's no dot in the way
                and (len(springs) == config[0] or springs[config[0]] != '#')    # It's the end or no more damaged left
            ):
                variations += self.__get_variations(springs[config[0] + 1:], config[1:])

        self.cache[key] = variations
        return variations
