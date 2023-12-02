from solution import Solution


class Solve(Solution):
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.raw_content = self.__read_file()

    @property
    def part_1(self) -> int:
        ret = 0
        for line in self.raw_content:
            num_str = ''
            for char in line:
                if char.isdigit():
                    num_str += char
            try:
                ret += int(num_str[0] + num_str[-1])
            except IndexError:
                pass
        return ret

    @property
    def part_2(self) -> int:
        num2words = {
            1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six',
            7: 'seven',
            8: 'eight',
            9: 'nine'
        }
        ret = 0
        for line in self.raw_content:
            num_str = ''
            for i, char in enumerate(line):
                if char.isdigit():
                    num_str += char
                else:
                    for key, val in num2words.items():
                        if line[i:].startswith(val):
                            num_str += str(key)
                            num_str += str(key)
                            break
            ret += int(num_str[0] + num_str[-1])
        return ret

    def __read_file(self) -> list[str]:
        with open(self.file_name, 'r') as fl:
            content = [line.strip('\n') for line in fl.readlines()]
        return content

