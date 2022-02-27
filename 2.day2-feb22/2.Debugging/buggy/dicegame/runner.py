from .die import Die
from .utils import i_just_throw_an_exception

class GameRunner:

    def __init__(self):
        ndices=2
        self.dice = Die.create_dice(ndices)
        self.reset()

    def reset(self):
        self.round = 1
        self.wins  = 0
        self.loses = 0

    def answer(self):
        total = 0
        for die in self.dice:
            total += die.value
        return total
    
    @classmethod
    def run(cls):        
        count_win_and_loss = cls()
        count_max_play = 0
        while True:
            
            print("Round {}\n".format(count_win_and_loss.round))

            runner = cls()
            for die in runner.dice:
                print(die.show())

            guess = input("Sigh. What is your guess?: ")
            guess = int(guess)

            if guess == runner.answer():
                print("Congrats, you can add like a 5 year old...")
                count_win_and_loss.wins += 1
                count_max_play += 1
            else:
                print("Sorry that's wrong")
                print("The answer is: {}".format(runner.answer()))
                print("Like seriously, how could you mess that up")
                count_win_and_loss.loses += 1
                count_max_play = 0
            print("Wins: {} Loses {}".format(count_win_and_loss.wins, count_win_and_loss.loses))
            count_win_and_loss.round += 1

            if count_max_play == 6:
                print("You won... Congrats...")
                print("The fact it took you so long is pretty sad")
                break

            prompt = input("Would you like to play again?[Y/n]: ")

            if prompt == 'y' or prompt == 'n':
                continue
            else:
                i_just_throw_an_exception()
