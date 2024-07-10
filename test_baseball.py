from unittest import TestCase
from baseball import BaseballGame


class TestBaseball(TestCase):

    def setUp(self):
        super().setUp()
        self.game = BaseballGame()

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
        self.assertEqual(1, 1)
