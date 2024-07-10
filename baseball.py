from game_result import GameResult


class BaseballGame:
    def __init__(self):
        self.question = "000"

    def guess(self, guess_number: str):
        self.assert_illegal_value(guess_number)
        if guess_number == self.question:
            return GameResult(True, 3, 0)
        else:
            strikes = 0
            for i in range(len(self.question)):
                char = guess_number[i]
                index = self.question.find(char)
                if index == i:
                    strikes += 1

            return GameResult(False, strikes, 0)

    def assert_illegal_value(self, guess_number):
        if guess_number is None:
            raise TypeError
        if len(guess_number) != 3:
            raise TypeError
        for number in guess_number:
            if not ord('0') <= ord(number) <= ord('9'):
                raise TypeError
        if self.is_duplicate_number(guess_number):
            raise TypeError

    def is_duplicate_number(self, g):
        return g[0] == g[1] or g[1] == g[2] or g[2] == g[0]
