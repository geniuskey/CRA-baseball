from unittest import TestCase
from baseball import BaseballGame
from game_result import GameResult


class TestBaseball(TestCase):

    def setUp(self):
        super().setUp()
        self.game: BaseballGame = BaseballGame()

    def assert_illegal_argument(self, guess_number):
        try:
            self.game.guess(guess_number)
            self.fail()
        except TypeError:
            pass

    def assert_matched_number(self, result, solved, strike, balls):
        self.assertIsNotNone(result)
        self.assertEqual(solved, result.get_solved())
        self.assertEqual(strike, result.get_strike())
        self.assertEqual(balls, result.get_balls())

    def test_exception_when_invalid_input(self):
        self.assert_illegal_argument(None)
        self.assert_illegal_argument("12")
        self.assert_illegal_argument("1234")
        self.assert_illegal_argument("12s")
        self.assert_illegal_argument("121")

    def generate_question(self, question_number):
        self.game.question: str = "123"

    def test_if_matched(self):
        self.generate_question("123")
        self.assert_matched_number(self.game.guess("123"), True, 3, 0)

    def test_if_unmatched(self):
        self.generate_question("123")
        self.assert_matched_number(self.game.guess("456"), False, 0, 0)

    def test_if_matched_partially(self):
        self.generate_question("123")
        self.assert_matched_number(
            self.game.guess("120"), False, 2, 0)
        self.assert_matched_number(
            self.game.guess("061"), False, 0, 1)
        self.assert_matched_number(
            self.game.guess("136"), False, 1, 1)
