# name = None;  # False
# # name = 10; True
# # name = 0; False
# # name = 1; True
# # name = -1; True
# # name = 0.0; False
# if name:
#     print('True : ', name);
# else:
#     print('False : ', name);
#
# if name:
#     print(10)
# else:
#     print(20);
#
# name = input("Enter Name");
#
# if name == 'durga':
#     print('Name is {}'.format(name));
# else:
#     print('Name is something else : {}'.format(name));
#
# name = input("Enter Name");
#
# if name == 'durga':
#     print('Name is %s' % name);
# else:
#     print('Name is something else : %s' % name);
#
# print('something {} and {}'.format(1, 2));
#
# name = input('Enter Values')
#
# if name == 'X':
#     print('X');
# elif name == 'Y':
#     print('Y');
# else:
#     print(name);
#
# firstValue = int(input("Enter First value to compare"));
# secondValue = int(input("Enter second value to compare"));
#
# print(firstValue if firstValue > secondValue else secondValue);  # Ternary operator
#
# if firstValue > secondValue:
#     print(firstValue);
# else:
#     print(secondValue);
#
#
# for x in range(20):
#     print(x, end=',');
# print();
# for x in range(0, 20, 9):
#     print(x, end=',',)
#
# # WHILE LOOP
#
# x = 0;
# while x < 10:
#     print('hello');
#     x = x+1;
# x = 0;
# while x in range(10):
#     print(x);
#     x = x+1;
#
#
# for x in range(15):
#     if x == 10:
#         print('break statement value : {}'.format(x));
#         break
#
# for x in range(100):
#     if x % 10 != 0:
#         continue
#     print(x);
#
#
# for x in range(10):
#     if x > 10:
#         break
#     print(x);
# else:
#     print('all range values are less than 10');
#
#
# def x1():
#     pass
#
#
# class A:
#     pass
#
#
# class B:
#     pass
#
#
# class C:
#     pass
#
#
# del C
# del A
# del B
# x = 10;
# del x;
#
# #  Check given number is primary or not
# primeNumber = int(input('Enter primary number to check'));
# if primeNumber == 1:
#     print('{} is not a primary number'.format(primeNumber));
# else:
#     for x in range(2, primeNumber):
#         if primeNumber % x == 0:
#             print('{} is not a primary number'.format(primeNumber));
#             break
#     else:
#         print('{} is a primary number'.format(primeNumber));
#
#
# #  Find Primary numbers below given number
#
# primaryNumberRange = int(input('Enter primary number range'));
# if primaryNumberRange <= 1:
#     print('No Primary number before provided range : {}'.format(primaryNumberRange));
# else:
#     for x in range(2, primaryNumberRange+1):
#         for y in range(2, x):
#             if x % y == 0:
#                 break
#         else:
#             print(x);


#  Print first n number of primary number

primaryNumberCount = int(input("Enter n number of primary number"));

count = 0;
number = 2;
if primaryNumberCount == 1:
    print(2);
else:
    while count < primaryNumberCount:
        for x in range(2, number):
            if number % x == 0:
                break
        else:
            print(number)
            count = count + 1;
        number = number + 1;

