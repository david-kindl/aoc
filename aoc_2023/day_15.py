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
    def part_2(self) -> any:
        boxes = self.__box_lenses()
        focusing_power = 0
        for box, content in boxes.items():
            for i, fl in enumerate(content.values()):
                focusing_power += (box + 1) * (i + 1) * fl
        return focusing_power

    def __parse(self):
        with open(self.file_name, 'r') as fl:
            sequence = [val for seq in fl.readlines() for val in seq.strip('\n').split(',')]
        return sequence

    def __box_lenses(self) -> dict[int, dict[str, int]]:
        boxes = {_: {} for _ in range(0, 256)}
        for seq in self.sequences:
            if '=' in seq:
                label, focal_length = seq.split('=')
                box = self.__build_hash(label)
                boxes[box][label] = int(focal_length)
            else:
                label = seq.split('-')[0]
                box = self.__build_hash(label)
                boxes[box].pop(label, None)
        return boxes

    @staticmethod
    def __build_hash(string: str) -> int:
        curr_value = 0
        for char in string:
            curr_value += ord(char)
            curr_value *= 17
            curr_value %= 256
        return curr_value
