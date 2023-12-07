from solution import Solution
from collections import Counter


class Solve(Solution):
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.hands = {
            (1, 1, 1, 1, 1): [[], []],
            (1, 1, 1, 2): [[], []],
            (1, 2, 2): [[], []],
            (1, 1, 3): [[], []],
            (2, 3): [[], []],
            (1, 4): [[], []],
            (5, ): [[], []],
        }
        self.__get_hands()

    @property
    def part_1(self) -> int:
        return self.__get_score(0)

    @property
    def part_2(self) -> int:
        return self.__get_score(1)

    def __get_score(self, dim: int) -> int:
        scores = []
        for grp in self.hands.values():
            st = sorted(grp[dim], key=lambda x: x[0])
            scores.extend([score[1] for score in st])
        return sum([score * (i + 1) for i, score in enumerate(scores)])

    def __get_hands(self) -> None:
        with open(self.file_name, 'r') as fl:
            for i, line in enumerate(fl.readlines()):
                hand, bid = line.split()
                self.__append_pt1_hand(hand, int(bid))
                self.__append_pt2_hand(hand, int(bid))

    def __append_pt1_hand(self, hand: str, bid: int) -> None:
        translated_hand = [self.__translate_card(card, 11) for card in hand]
        counter = Counter(translated_hand)
        grp = tuple(sorted(list(counter.values())))
        self.hands[grp][0].append((translated_hand, bid))

    def __append_pt2_hand(self, hand: str, bid: int) -> None:
        translated_hand = [self.__translate_card(card, 1) for card in hand]
        counter = Counter(translated_hand)
        if 1 in counter.keys() and counter[1] < 5:
            joker = sorted(
                {key: value for key, value in counter.items() if key != 1}.items(),
                key=lambda x: (x[1], x[0]),
                reverse=True
            )[0]
            counter[joker[0]] += counter[1]
            del counter[1]
        grp = tuple(sorted(list(counter.values())))
        self.hands[grp][1].append((translated_hand, bid))

    @staticmethod
    def __translate_card(card: str, joker: int) -> int:
        translator = {'T': 10, 'J': joker, 'Q': 12, 'K': 13, 'A': 14}
        try:
            val = translator[card]
        except KeyError:
            val = int(card)
        return val


if __name__ == '__main__':
    solution = Solve('/home/david/repo/aoc/cache/2023/day_7.txt')
    print(solution)
