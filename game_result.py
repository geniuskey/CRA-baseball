class GameResult:
    def __init__(self, solved, strike, balls):
        self.__solved = solved
        self.__strike = strike
        self.__balls = balls

    def get_solved(self):
        return self.__solved

    def get_strike(self):
        return self.__strike

    def get_balls(self):
        return self.__balls


