
# defining a user defined function
# def is a keyword to define the function
def add(a, b):
    print(f'add : {a+b}');


add(10, 20);
add(100, 200);
add(1000, 2000);


def subst(a, b):
    print(f'sub : {a-b}');


subst(20, 10);
subst(200, 100);
subst(2000, 1000);


def wish():
    print('Hello world , welcome to python programming');


wish();


def wish():
    print('Hello world , previous wish will be replaced with this same method');


wish();
# add(); ERROR : must pass the arguments


def multiply(a=10, b=4):
    print(a, b);
    return a*b;


print(multiply(10, 20));


def factorial(number):
    if number == 0:
        return 1;
    if number >= 1:
        return number * factorial(number-1);



for i in [factorial(x) for x in range(11)]:
    print(i, end=' ');
print();


def x():
    return 'a', 'b';  # internally uses tuple


# unpacking tuple
x, y = x();
print(x, y);

# keyword argument calling
print(multiply(a=10, b=20));
# keyword and positional calling
print(multiply(10, b=20));
# positional parameters calling
print(multiply(10, 20));
# using default values
print(multiply());
print(multiply(10, 9));
print(multiply(8));


def example():
    pass;


def example(a, b):
    pass;


def example(a=10, b=20):
    pass;


def example(a, b=0):
    pass;


# def example(a=0, b):
#     pass;
# ERROR : Default values should be last in the method parameters
# SyntaxError: non-default argument follows default argument


# variable length argument declaration
def var_args(*a):
    print(type(a));  # TUPLE
    for x in a:
        print(x)


var_args(1, 2, 3, 5)


def test(**kwargs):
    print(type(kwargs));


test();
test(a='aa', n='bb');

def print_kwargs(**kwargs):
    print(kwargs)


print_kwargs(kwargs_1="Shark", kwargs_2=4.5, kwargs_3=True)



def test(*m, x=10):
    print(m);
    print(x);


test(1, 2, 3);
test(1, 2, 3, x=20);


def test(m, *x):
    print(m);
    print(x);


test(1, 2, 3);
test(2, 3, 20);


def test(a, b, c=10, d=20):
    print(a, b, c, d);


# test();  # INVALID
# test(10);  # INVALID
test(10, 20);
test(10, 20, 30);
test(10, 20, 30, 40);

test(a=10, b=30);
test(c=20, d=10, a=10, b=1);
# test(a=10, b=20, 30, 40);  # INVALID
# test(10, 20, a=10, b=30);


def test(a, b, *c, **d):
    pass;


# INVALID
# def test(*a, *b):
#     pass;


def test(*a, **kwargs):
    pass;



# INVALID
# def test(**a, **b):
#     pass;



# INVALID
# def test(**ks, *a, b, c):
#     pass;


def test(a, b, *c, **d):
    pass;


global_variable = 10;

def x():
    print(global_variable);



def y():
    a = 10;
    print(a);


# def z():
#    # print(a); ERROR


def x():
    global global_variable;
    global_variable = 20;
    print(global_variable);


# x();


def y():
    print(global_variable);


# y();


print(globals());
print(globals()['global_variable']);
globals()[global_variable] = '1bnv';
print(globals()[global_variable]);


def factorial(n):
    return 1 if n == 0 else n * factorial(n-1);


for n in range(1, 11):
    print(factorial(n));


# LAMBDA
lambda a: a*a;
lambda a: 2**a;
lambda a, b: a*b;
lambda a, b: a if a > b else b;
lambda a, b, c: a if a > b and a > c else b if b > c else c;


# passing function to another function with arguments
def call(function, sequence):
    function(sequence);


# calling a function by passing a function
call(factorial, 10);



def iseven(digit):
    return True if digit % 2 == 0 else False;


for i in range(11):
    if iseven(i):
        print('Even number : ', i);


# Using filter method to filter non even numbers
for even_number in filter(lambda a: a % 2 == 0, range(11)):
    print('Even number : ', even_number);


# Using map function to the given sequence
for square in map(lambda a: a*a, range(10)):
    print('square of the number : ', square);


for upper in map(lambda name: name.swapcase(), {'1Bc', 'b', 'C'}):
    print(upper);