from solution import Solution


class Solve(Solution):
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.raw_data = self.__get_raw_data()
        self.cards = self.__parse()
        self.score_cards = self.__get_scores()

    @property
    def part_1(self) -> any:
        cum_score = 0
        for score in self.score_cards.values():
            cum_score += score[1]
        return cum_score

    def part_2(self) -> any:
        pass

    def __get_raw_data(self):
        with open(self.file_name, 'r') as fl:
            content = [line.strip('\n') for line in fl.readlines()]
        return content

    def __parse(self):
        cards = {}
        for line in self.raw_data:
            card_id, num_sets = line.split(':')
            card_id = int(card_id[card_id.find(' ') + 1:])
            cards[card_id] = self.__get_sets(num_sets)
        return cards

    @staticmethod
    def __get_sets(num_sets: str) -> tuple[list[str], list[str]]:
        set_1, set_2 = num_sets.split('|')
        set_1 = set_1.strip().split()
        set_2 = set_2.strip().split()
        return set_1, set_2

    def __get_scores(self):
        scores = {}
        for card, sets in self.cards.items():
            scores.setdefault(card, [0, 0, 0])
            for s in sets[0]:
                if s in sets[1]:
                    scores[card][0] += 1
            score_cnt = scores[card][0]
            score_base = 1 if score_cnt > 0 else 0
            score_mod = 2 ** (score_cnt - 1)
            scores[card][1] = score_base * max(1, score_mod)
        return scores
