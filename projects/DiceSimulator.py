import NumberGuessingGame;
import random;


def play_game():
    while True:
        dice_count:int = NumberGuessingGame.get_positive_number('How many dice would you like to roll? ');
        while dice_count > 0:
            print(random.choice(range(1,7)),  end= ', ');
            dice_count = dice_count - 1;
        print();
        play_again:str = input('Do you want to play again? (YES/NO) : ');
        if play_again.lower() == 'no':
            print('Thanks for playing....')
            break;


if __name__ == '__main__':
    play_game();
