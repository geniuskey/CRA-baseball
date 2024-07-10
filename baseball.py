from game_result import GameResult


class BaseballGame:
    def __init__(self):
        self.question = "000"

    def guess(self, guess_number: str):
        self.assert_illegal_value(guess_number)
        if self.is_solved(guess_number):
            return self.get_success_game_result()
        else:
            balls, strikes = self.get_unsolved_game_result(guess_number)

            return GameResult(False, strikes, balls)

    def is_solved(self, guess_number):
        return guess_number == self.question

    def get_success_game_result(self):
        return GameResult(True, 3, 0)

    def get_unsolved_game_result(self, guess_number):
        strikes = 0
        balls = 0
        for i in range(len(self.question)):
            if self.question.find(guess_number[i]) == i:
                strikes += 1
            elif self.question.find(guess_number[i]) > -1:
                balls += 1
        return balls, strikes

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
