from solution import Solution


class Solve(Solution):
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.hist = self.__get_hist()

    @property
    def part_1(self) -> any:
        ret = 0
        for line in self.hist:
            ret += sum([elem[-1] for elem in self.__predict_item(line)])
        return ret

    @property
    def part_2(self) -> any:
        ret = 0
        for line in self.hist:
            ret += sum(elem[0] * ((-1) if i % 2 == 1 else 1) for i, elem in enumerate(self.__predict_item(line)))
        return ret

    def __get_hist(self):
        hist = []
        with open(self.file_name, 'r') as fl:
            for line in fl.readlines():
                hist.append(list(map(int, line.split())))
        return hist

    @staticmethod
    def __predict_item(hist: list[int]) -> list[list[int]]:
        if not isinstance(hist[-1], list):
            hist = [hist]
            while len(hist[-1]) > 1:
                curr_line = [elem for elem in hist[-1]]
                hist.append([curr_line[i + 1] - curr_line[i] for i in range(len(curr_line) - 1)])
        return hist
