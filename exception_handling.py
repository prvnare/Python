print('Hello world');
# print(19/0); ZeroDivisionError: division by zero
print('End');



print('Hello World');
try:
    print(10/0);
except ZeroDivisionError as error:
    print(type(error));
    print(error.__class__.__name__);
    print(error);
    print(10/2);
print('End');



try:
    x = int(input('enter the first value'));
    y = int(input('enter the first value'));    
    print(x/y);
except ValueError as error:
    print(error);
    print(error.__class__.__name__);
except ZeroDivisionError as error:
    print(error);
    print(error.__class__.__name__);
except BaseException as error:
    print(error);
    print(error.__class__.__name__);



try:
    x = int(input('enter the first value'));
    y = int(input('enter the first value'));    
    print(x/y);
except BaseException as error:
    print(error);
    print(error.__class__.__name__);



try:
    x = int(input('enter the first value'));
    y = int(input('enter the first value'));    
    print(x/y);
except (ValueError,ZeroDivisionError,BaseException) as error:
    print(error);
    print(error.__class__.__name__);

from os import _exit;

try:
    print(10/0);
except:
    print('except');
finally:
    print('finally');

try:
    print('hello world');
    _exit(0);
except:
    print('except block');
finally:
    print('finally block');

try:
    print('something');
finally:
    print('');