import random;

class RPS:
    def __init__(self):
        print('Welcome to RPS 9000');
        self.user_won = 0;
        self.ai_won = 0;
        self.moves: dict = {'rock' : '🪨', 'paper' : '📜', 'scissors': '✂️'};
        self.valid_moves:list[str] = [key for key in self.moves.keys()];


    def play_game(self):
        user_choice = input('Rock Paper or Scissors >> ').lower();
        if user_choice not in self.valid_moves:
            print('Please choose valid move..');
            self.play_game();

        ai_choice  = random.choice(self.valid_moves);
        self.disply(user_choice, ai_choice);
        self.check_result(user_choice, ai_choice);
        print(f'winning count  --> AI : {self.ai_won} , USER : {self.user_won} ')


    def disply(self, user_choice, ai_choice):
        print('---------');
        print(f'You choose -- {self.moves[user_choice]}');
        print(f'AI choose -- {self.moves[ai_choice]}');
        print('---------');


    def check_result(self, user_choice, ai_choice):
        if user_choice == ai_choice :
            print("It's a tie ...");
        elif user_choice == 'rock' and ai_choice == 'scissors':
            print('You Won...');
            self.user_won += 1;
        elif user_choice == 'paper' and ai_choice == 'rock':
            print('You win.');
            self.user_won += 1;
        elif user_choice == 'scissors' and ai_choice == 'paper':
            print('You win.');
            self.user_won += 1;
        else :
            print('AI win.');
            self.ai_won += 1;

        

if __name__ == '__main__':
    rps = RPS();
    while True:
        rps.play_game();
        print();


