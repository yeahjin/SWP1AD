from tongman import Tongman
a = Tongman()

def new_game():
    a.newGame()
    return {'code' : 'success'}

def guess(d):
    guess = d.get('guess',[''])[0]
    b = a.guess(guess)
    c = a.secretnum
    trials = a.tryed()
    return {'a':guess,'code': 'success','num': a.gameover, 'trials': trials,'secre':c}