from unittest import TestCase
from baseball import BaseballGame

class TestBaseball(TestCase):
    def test_exception_when_input_is_none(self):
        self.game = BaseballGame()
        with self.assertRaises(TypeError):
            self.game.guess(None)

    def test_game(self):
        self.assertEqual(1,1)
