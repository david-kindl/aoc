from solution import Solution


class Solve(Solution):
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.time, self.distance = self.__get_data()

    @property
    def part_1(self) -> any:
        time = list(map(int, self.time.split()))
        dist = list(map(int, self.distance.split()))
        val = 1
        for i in range(len(time)):
            s = self.solve(time[i], dist[i])
            val *= s
        return val

    @property
    def part_2(self) -> any:
        time = int(self.time.replace(' ', ''))
        dist = int(self.distance.replace(' ', ''))
        val = self.solve(time, dist)
        return val

    def __get_data(self):
        with open(self.file_name, 'r') as fl:
            times = fl.readline().split(':')[1].strip()
            distance = fl.readline().split(':')[1].strip()
        return times, distance

    @staticmethod
    def solve(time: int, dist: int) -> int:
        b = time
        c = dist
        div = (b ** 2 - 4 * c) ** (1 / 2)
        pt1 = -(-((b + div) / 2 - 1) // 1)
        pt2 = ((b - div) / 2) // 1
        return int(pt1 - pt2)
