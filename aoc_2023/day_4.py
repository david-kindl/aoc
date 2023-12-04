from solution import Solution


class Solve(Solution):
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.raw_data = self.__get_raw_data()
        self.cards = self.__parse()

    @property
    def part_1(self) -> any:
        cum_score = 0
        for card, attr in self.cards.items():
            score = attr['score']
            score_base = 1 if score > 0 else 0
            score_mod = 2 ** (score - 1)
            cum_score += score_base * max(1, score_mod)
        return cum_score

    @property
    def part_2(self) -> any:
        cards_won = {i: 1 for i in self.cards}
        for card, attr in self.cards.items():
            score = attr['score']
            rng = cards_won[card] * [i + 1 for i in range(score)]
            for j in rng:
                cards_won[card + j] += 1
        return int(sum([val for val in cards_won.values()]))

    def __get_raw_data(self):
        with open(self.file_name, 'r') as fl:
            content = [line.strip('\n') for line in fl.readlines()]
        return content

    def __parse(self):
        cards = {i + 1: {} for i in range(len(self.raw_data))}
        for i, line in enumerate(self.raw_data):
            card = i + 1
            num_sets = line.split(':')[1]
            cards[card]['sets'] = self.__get_sets(num_sets)
            cards[card]['score'] = self.__get_scores(cards[card]['sets'])
        return cards

    @staticmethod
    def __get_sets(num_sets: str) -> tuple[set[str], set[str]]:
        set_1, set_2 = num_sets.split('|')
        set_1 = set(set_1.strip().split())
        set_2 = set(set_2.strip().split())
        return set_1, set_2

    @staticmethod
    def __get_scores(sets: tuple[set[str], set[str]]) -> int:
        return len(sets[0] & sets[1])
