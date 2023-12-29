import random;


def is_postive(number:int):
    if number <= 0:
        print('Enter number greater than ZERO');
        return None;
    return number;


def get_number( msg:str, guessing:int = 0) -> int :
    try:
        return is_postive(int(input(msg)) if guessing <= 0 else guessing);
    except ValueError :
        print('Enter valid number');


def get_positive_number(msg:str):
    number: int = None;
    while True:
        number = get_number(msg);
        if number:
            break;
    return number;


def verify(generated_number):
    count:int = 4;
    while True:
        if count == 0:
            print(f'GAVE OVER --- Actual Number : {generated_number}');
            break;
        
        guessed_number:int = get_positive_number('Guess Number : ');
        count = count - 1;
        if generated_number == guessed_number:
            print(f'Guessed correctly  ---  actual Number : {generated_number} , guessed number : {guessed_number}');
            break;
        elif guessed_number > generated_number:
            print(f'{"Number is higher. enter low number" if count > 0 else ""}');
        else:
            print(f'{"Number is low. enter higher number" if count > 0 else "" }');
       
        
def play_game():
    number_range :int = get_positive_number('Enter guessing number range from 1 to : ');
    print(f'guess the number in the range of 1 to {number_range}');
    generated_number = random.choice([i for i in range(1, number_range+1)]);
    verify(generated_number);
    
if __name__ == '__main__':
    play_game();