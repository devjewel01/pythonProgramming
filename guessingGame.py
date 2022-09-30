import random

class BinarySearch:
    def __init__(self):
        self.number = random.randint(1, 100)
        self.guess = None

    def guessNumber(self):
        try:
            self.guess = int(input("Guess a number : "))
            if self.guess<0 or self.guess>100:
                print("you should game between 1 and 100")
                return False
        except ValueError:
            print('Not a valid guess.')
            return False
        return True

class GuessingGame(BinarySearch):
    def play(self):
        print("Welcome to Guessing Game!")
        print("I am thinking of a number between 1 and 100")
        while True:
            if not self.guessNumber():
                continue
            if self.guess < self.number:
                print("lower!")
            if self.guess > self.number:
                print("higher!")
            if self.guess == self.number:
                print("It's match!")
                break


if __name__ == "__main__":
    game = GuessingGame()
    game.play()