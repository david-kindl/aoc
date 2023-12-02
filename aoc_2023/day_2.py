from functools import reduce
from solution import Solution


class Solve(Solution):
    stone_numbers = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.games = self.__get_games()

    @property
    def part_1(self) -> int:
        return sum([k for k, v in self.games.items() if v['is_valid']])

    @property
    def part_2(self) -> int:
        return sum([v['power_of_set'] for k, v in self.games.items()])

    def __get_games(self) -> dict[int, dict[str, any]]:
        games = {}
        with open(self.file_name, 'r') as fl:
            for line in fl.readlines():
                game_id, trials = line.strip('\n').split(':')
                game_id = self.__get_game_id(game_id)
                trials = self.__get_trials(trials)
                games[game_id] = trials
        return games

    @staticmethod
    def __get_game_id(line: str) -> int:
        return int(line[line.find(' ') + 1:])

    def __get_trials(self, line: str) -> dict[str, any]:
        trials_log = {
            'red': 0,
            'green': 0,
            'blue': 0,
            'is_valid': True
        }
        trials = [val.split(',') for val in line.split(';')]
        for trial in trials:
            for t in trial:
                cnt, color = t.split()
                trials_log[color] = max(int(cnt), trials_log[color])
                trials_log['is_valid'] = trials_log['is_valid'] and self.stone_numbers[color] >= trials_log[color]
        trials_log['power_of_set'] = reduce((lambda x, y: x * y), [v for k, v in trials_log.items() if k != 'is_valid'])
        return trials_log
