from solution import Solution


class Solve(Solution):
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.__get_pipes()

    @property
    def part_1(self) -> any:
        return int((len(self.__get_loop()) + 1) / 2)

    @property
    def part_2(self) -> any:
        pass

    def __get_start_dirs(self) -> list[tuple[int, int]]:
        ret = []
        start_x, start_y = self.start_loc
        for x, y in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            curr_x, curr_y = start_x + x, start_y + y
            if curr_x not in (self.x_len, -1) and curr_y not in (self.y_len, -1):
                print(curr_x, curr_y)
                curr_node = self.pipes[curr_y][curr_x]
                if self.start_loc in self.__decode_pipes(curr_x, curr_y, curr_node):
                    ret.append((x, y))
        return ret

    def __get_pipes(self) -> None:
        """
        Parsing the input and locating the start position
        :return: None
        """
        pipes = []
        with open(self.file_name, 'r') as fl:
            for i, line in enumerate(fl.readlines()):
                pipes.append(line.rstrip('\n'))
                s_loc = line.find('S')
                if s_loc > -1:
                    self.start_loc = (line.find('S'), i)
        self.pipes = pipes
        self.x_len = len(pipes[0])
        self.y_len = len(pipes)

    @staticmethod
    def __decode_pipes(x: int, y: int, pipe: str) -> tuple[tuple[int, int]]:
        translator = {
            'F': ((x, y + 1), (x + 1, y)),
            '-': ((x - 1, y), (x + 1, y)),
            '7': ((x - 1, y), (x, y + 1)),
            '|': ((x, y - 1), (x, y + 1)),
            'J': ((x, y - 1), (x - 1, y)),
            'L': ((x + 1, y), (x, y - 1)),
            '.': ((), ())
        }
        return translator[pipe]

    def __get_loop(self) -> list[tuple[int, int]]:
        """
                Mimicking a doubly linked list
                :return: Max distance from the start node
                """
        directions = self.__get_start_dirs()
        dist = []
        for direction in directions:
            curr_x, curr_y = self.start_loc
            next_x, next_y = curr_x + direction[0], curr_y + direction[1]
            while self.start_loc != (next_x, next_y):
                neighbours = self.__decode_pipes(next_x, next_y, self.pipes[next_y][next_x])
                next_loc = [(x, y) for x, y in neighbours if (x, y) != (curr_x, curr_y)][0]
                dist.append((curr_x, curr_y))
                curr_x, curr_y = next_x, next_y
                next_x, next_y = next_loc
            return dist

    def __str__(self):
        directions = self.__get_loop()
        prnt = ''
        for i, line in enumerate(self.pipes):
            for j, pipe in enumerate(line):
                if pipe == '.':
                    prnt += '\033[31m' + pipe
                elif (j, i) in directions:
                    prnt += '\033[32m' + pipe
                else:
                    prnt += '\033[37m' + pipe
            prnt += '\n'
        return '\n'.join((super().__str__(), prnt))


if __name__ == '__main__':
    s = Solve('/home/david/repo/aoc/cache/2023/day_10.txt')
    print(s)
