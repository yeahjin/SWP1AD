import random

class Tongman:
    def __init__(self):
        self.secretnum = 0
        self.trials = 0
        self.gameover = False

    def newGame(self):
        self.secretnum = random.randint(1,16)
        self.trials = 0
        self.gameover = False

    def guess(self,userGuess):
        if self.secretnum == int(userGuess):
            self.trials += 1
            self.gameover = True
        else:
            self.trials += 1

    def tryed(self):
        return self.trials



if __name__ ==  "__main__":
    a = Tongman()
    a.newGame()
    while a.gameover != True:
        uinput = int(input())
        a.guess(uinput)
    print(a.tryed())
