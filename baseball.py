class BaseballGame:
    def guess(self, guess_number: str):
        if guess_number is None:
            raise TypeError

        if len(guess_number) != 3:
            raise TypeError

        for number in guess_number:
            if not ord('0') <= ord(number) <= ord('9'):
                raise TypeError

        g = guess_number
        if g[0] == g[1] or g[1] == g[2] or g[2] == g[0]:
            raise TypeError
