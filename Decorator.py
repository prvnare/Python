# Decorator concept

def function():
    print('Hello world, welcome to python programming ');

# Calling a function here
function();

# print the funtion 
print(function); # prints the Funtion class object details here
print(id(function)); # prints the address of funtion object;
print(type(function)); # Prints the type of the  Object 

# poiniting one more reference variable to the function object 
alias = function;

# verifying alias and function are same ?
print(alias is function);

# calling a funciton 
alias();
function();

# defining a funciton which is having an inner function
def outerfunction():
    print('Outer function');
        # defining an inner function inside another fucntion here
    def innerfunction():
        print('inner function');
    # here we are not making the function call instead we are returning the function object 
    return innerfunction;

# calling outer function here which returns an other funtion reference 
# not holding the function reference here
outerfunction();

# holding the reference of the another funtion which is returning by the outer function 
function_object = outerfunction();

# calling the innerfunction()
function_object();

# passing a function as an argument to the other function

def outerfunction(function):
    print('outer function which takes another function as an input');
    # calling a input function
    function();

def temporary_function():
    print('i am a temporary function which do nothing');

# passing temporary_function as an argument to the outerfunction
outerfunction(temporary_function);


# Decorator is a normal function which takes a funcion as input and returns a function as output like 

# Defining a decorator here : outerfunction is a decorator
def outerfunction(function):
    print('outer function which takes another function as an input');
    def inner_function():
        # calling a input function
        function();
    return inner_function;



# Using Decorator
@outerfunction
def function():
    print('Hello i am a noraml function using a decorator');

function();

# Decorator chaining

@outerfunction
@outerfunction
@outerfunction
@outerfunction
@outerfunction
@outerfunction
@outerfunction
@outerfunction
@outerfunction
def hello():
    print('hello ');

hello();

#using decorator chanining

def chain_one(function):
    print('chain_one');
    print(function);
    print(id(function));
    def inner_function_one():
        print('chain_one -- inner_function');
        function();
    return inner_function_one;

def chain_two(function):
    print('chain_two');
    print(function);
    print(id(function));
    def inner_function_two():
        print('chain_two inner_function');
        function();
    return inner_function_two;

def chain_four(function):
    print('chain_four');
    print(function);
    print(id(function));
    def inner_function_four():
        print('chain_four inner_function');
        function();
    return inner_function_four;

def chain_three(function):
    print('chain_three');
    print(function);
    print(id(function)); 
    def inner_function_three():
        print('chain_three  inner_funtion');
        function();
    return inner_function_three;


# takes chain_three inner_fuction as input
@chain_four
# takes chain_two inner_function as input
@chain_three
# takes chain_one inner_function as input
@chain_two
# takes disply function as input
@chain_one
def disply():
    print('disply function to disply something here');


# execution starts from the chain_four inner_function onwords
disply();