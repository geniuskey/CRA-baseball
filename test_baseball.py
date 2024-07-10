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

    def test_exception_when_invalid_input(self):
        self.assert_illegal_argument(None)
        self.assert_illegal_argument("12")
        self.assert_illegal_argument("1234")
        self.assert_illegal_argument("12s")
        self.assert_illegal_argument("121")

    def test_game(self):
        self.game.question: str = "123"
        result: GameResult = self.game.guess("123")
        self.assertIsNotNone(result)
        self.assertTrue(result.solved)
        self.assertEqual(3, result.strikes)
        self.assertEqual(0, result.balls)

