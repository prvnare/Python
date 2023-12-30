import string;
import secrets;
from NumberGuessingGame import get_positive_number as get_int;


def contain_uppercase(password:str) -> bool:
    for char in password:
        if char.isupper():
            return True;
    return False;


def contain_specialcase(password:str) -> bool:
    for char in password:
        if char in string.punctuation:
            return True;
    return False;


def generate_password(length: int, symbol:bool, uppercase:bool) -> str:
    password_chars =  string.ascii_lowercase + string.digits;

    if symbol:
        password_chars += string.punctuation;

    if uppercase:
        password_chars += string.ascii_uppercase;

    new_password = '';

    for i in range(length):
        new_password +=  password_chars[secrets.randbelow(len(password_chars))];
    
    return new_password;


def verify_check(password, symbol, uppercase):
    if symbol and uppercase :
        return contain_uppercase(password) and contain_specialcase(password);
    elif symbol:
        return contain_specialcase(password);
    elif uppercase:
        return contain_uppercase(password);
    else:
        return True;


if __name__ == '__main__':
    number:int = get_int('Enter the number of the passwords required ? ');
    length:int = get_int('Enter the length of the password : ');
    upper_enabled:str = input('Do you want Upper case in password? (yes/no) :  ').lower();
    speacial_chars_enabled:str = input('Do you want special charecters in password? (yes/no) : ').lower();
    print('*' * 30);
    for i in range(1, number+1):
        while True:
            new_password:str = generate_password(length=length,
                                            uppercase= True if upper_enabled == 'yes' else False,
                                            symbol=True if speacial_chars_enabled == 'yes' else False);
            if verify_check(new_password, True if speacial_chars_enabled == 'yes' else False, True if upper_enabled == 'yes' else False):
                print(f' {i} --> {new_password}  (U : {contain_uppercase(new_password)}, S : {contain_specialcase(new_password)}) ');
                break;



