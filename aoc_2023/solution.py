from os import path
from abc import ABC, abstractmethod


class Solution(ABC):
    @property
    @abstractmethod
    def part_1(self) -> any:
        pass

    @property
    @abstractmethod
    def part_2(self) -> any:
        pass

    def __str__(self):
        header = path.splitext(path.basename(__file__))[0]
        pt1 = f'Solution to part 1 is: {self.part_1}'
        pt2 = f'Solution to part 2 is: {self.part_2}'
        return '\n'.join((header, pt1, pt2))
