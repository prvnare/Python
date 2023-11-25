# INPUT AND OUTPUT Operations

from sys import *

# inputValue = input('Enter a input value');
# print(type(inputValue));
#
# inputValue = eval(input('Enter a input value'));
# print(inputValue);
# print(type(inputValue));


# firstValue, secondValue = [int(x) for x in input('enter values').split()];
# print(firstValue+secondValue);

# inputValue = eval(input('Enter a input value : '));
# print(inputValue);
# print(type(inputValue));
#
# inputValue = '[1,2]';
# # print(eval(inputValue));
# # inputValue = """Enter a input value : """;
# inputValue = eval(inputValue);
# print(inputValue);
# print(type(inputValue));

print(type(argv));

for x in range(1, 11):
    print(x);


print(10, 20, 30, 'a', sep=':', end='^^^^');
print(10, 20, 30, 'a', sep=':', end='^^^^');
print()

print('{}{}{}'.format(1, 2, 3));