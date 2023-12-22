from sys import *;
def print_star(msg):
    print('*' * 30);
    print(msg)
    print('*' * 30);

# creating a string object 
first_way  = 'Hello World';
second_way = str('Hello World');
#third_way = input('Enter a string : ');
print_star('String object creation');

# printing the id or reference number of the string object and object type
print('Using quotes creating string object :','-->',first_way, id(first_way), '-->',type(first_way));
print('Using str function to create the string object : ', '-->', second_way, id(second_way), '-->',type(second_way));
# print('By reading input from the keyboard and creating the string object : ','-->', third_way,id(third_way), '-->',type(third_way));

print_star('Accessing elements using index');

# accessing the elements of string
    # Using index --> as string is a index based object
school_name = 'GMS Grameena Vikas School';

print(school_name[0])  # index starts from 0 to len(str);
print(school_name[13]); # V

    # accessing the index element which is not available always throws an error
# print(school_name[100]); EXCPTION  # string index out of rang 

    # Negative indexing is possible in python
print(school_name[-1]);  # l --> access the elements from end of the string
# print(school_name[-100]); #EXCPTION  # string index out of rang 
print_star('printing all the indices of the string elements');
    # print all the negetive and posstive index of the element in the present in a string
    # Using while
index = 0;
while index < len(school_name):
    print(f'{school_name[index]} element at positive index : {index} and negeative index : {index -len(school_name)}');
    index = index + 1;
print_star('printing using for loop');

    # Using for loop
for index in range(0, len(school_name)):
     print(f'{school_name[index]} element at positive index : {index} and negeative index : {index -len(school_name)}');
print_star('printitng all the elemenets one afer other');
# print all the elements of the string 

for i in range(0, len(school_name)):
    print(school_name[i],  end='--');

print()
print_star('Accessing elements using slice operator');

# Accessing elements using slice operator
    # [begin : end : step]
    # STEP shold not be a 0
    # STEP default value is 1
    # STEP value can be postive or negative value
    # if postive --> forward direction starting index from 0
    # if negativ --> backward direction starting index -1

    # Uing positive indexs
print(school_name[::]); # prints all the elements in the string from begin : 0 to end : last index , step = 1
print(school_name[0:5]); #  GMS G --> (begin = 0,end = 4,step = 1) 
print(school_name[:10]); # GMS Gramee  --> (begin = 0, end = 9, step = 1)
print(school_name[5:7]); # ra --> (begin = 5, end = 6, step = 1)
print(school_name[0:1000]); # GMS Grameena Vikas School --> (begin = 5, end = 999, step = 1) wont throw index out of exception 
print(school_name[100:1000]); # Empty value --> (begin = 100, end = 999, step = 1) wont throw index out of exception 
print(school_name[10:2]); # Empty value --> (begin = 10, end = 1, step = 1)  we wont get indez 1 after 10th index
print(school_name[0:0]); # EMPTY
print(school_name[-10:-17]) # EMPTY  --> (begin = -10, end = -18, step = 1)  we wont get index -10 in forward direction

    # STEP deafult is 1 with forward direction
    # begin default in forward direction in 0
    # end default in forward direction is till last element of the string and wont throw any ERROR if end is out of range 
print(school_name[::2]); # GSGaen ia col --> (begin = 0, end = last Index, step = 2)
print(school_name[1:10:2]); # M rme  --> (begin = 1, end = 9, step = 2)
print(school_name[1:1000:2]); # M rmeaVksSho  --> (begin = 1, end = 999, step = 2)
print(school_name[10:8:3]); #EMPTY --> (begin = 10, end = 7, step = 3) in forward direction we wont get 8 index after the 10th index

print_star('Accessing elements using slice with negatic indices');
    # Uing negative indexs
print(school_name[::-1]) # loohcS sakiV aneemarG SMG -->  (begin = -1, end = -len(string), step = -1) backword direction 
print(school_name[-10:-22:-1])# -->kiV aneemarG  (begin = -10, end = -21 (-22+1), step = -1) backword direction
print(school_name[10:1:-1]) # neemarG S --> (begin = 10, end = 2 (1+1), step = -1) backword direction
print(school_name[10::-1]); # neemarG SMG -->(begin = 10, end = 0, step = -1) backword direction
print(school_name[0:10:-1]);# EMPTY
print(school_name[-1000:1000:-1]); # EMPTY as we wont get 1000 index after -1000 in backword direction
print(school_name[1000:-1000:-1]); # loohcS sakiV aneemarG SMG -->(begin = 1000, end = -999, step = -1) backword direction
print(school_name[110:10:-1]);# loohcS sakiV a -->(begin = 110, end = 11 (10+1), step = -1) backword direction
print(school_name[-100:-200: -10]); # Empty
print(school_name[:0:-1]); # loohcS sakiV aneemarG SM -->(begin = -1, end = 1 (0+1), step = -1) backword direction
print(school_name[0:-10:-1]);  # EMPTY
print(school_name[-10:-1:-1]); # EMPTY
print(school_name[100:-1:-1]); # EMPTY  -->(begin = 100, end = 0 (-1+1), step = -1) backword direction
print(school_name[-100:-1:-1]); #EMPTY
print(school_name[-100:-1000:-1]); #EMPTY
print(school_name[-5:-100:-1]); # cS sakiV aneemarG SMG -->(begin = 100, end = -99 (-100+1), step = -1) backword direction
print(school_name[100:-100:-1]); # loohcS sakiV aneemarG SMG -->(begin = 100, end = -99, step = -1) backword direction
print(school_name[100:0:-1]);# loohcS sakiV aneemarG SM

print(school_name[10::]); # na Vikas School
print(school_name[10::-1]); # neemarG SMG

print(school_name[100:-100:-1]); # loohcS sakiV aneemarG SMG
print(school_name[-1::-1]); # loohcS sakiV aneemarG SMG
print(school_name[:-3:-1]); #lo
print(school_name[-100:-1000:-1]); # EMPTY
print(school_name[0:1000]); # GMS Grameena Vikas School
print(school_name[0:1000:-1]); # Empty
print(school_name[0:-1:-1]); # Empty

print(school_name[10:-1:-1]); # Empty
print(school_name[-10:-1:-1]); # Empty
print(school_name[-10:-1000:-1]); # kiV aneemarG SMG

print_star('Object immutablity');

# String is an immutable object 
# if perform any change in the existing object new object will be created with new changes

current_string = 'Hello World';
temp = current_string;
print('Before changing the content of the string : ---> ');
print(id(current_string));
print(current_string);
print('After changing the content of the string : ---> ');
current_string = current_string + 'Name';
print(id(current_string));
print(current_string);
print('pevious id : ', id(temp));
print('after changing id', id(current_string));

print_star('Performing arithmatic operators ')

print('using (+) to concate 2 strings');
print('{} + {} --> {}'.format('Hello','World', 'Hello'+'World'));
    # both oparends should be string only  (string) + (string) --> possible scenario
# print('a' + 1); # TypeError: can only concatenate str (not "int") to str

print('String repetation using  * operator');
print('hello' * 2);
print(2 * 'Hello');
print('using integer in binary format (0B1010) --> ', 0B1010 * 'Hello');
print('using integer in ocatal format (0O003) --> ', 0O003 *  'Hello');
print('using integer in Hexa Decimal format (0XA) --> ', 0XA * 'Hai');

    # while using * , one operator should in integer and other should be in string, other objects are not allowed
# print('using one oparend float (1.0)' ,1.0 * 'hello'); # TypeError: can't multiply sequence by non-int of type 'float'

print_star('Using membership operators ("in", "not in")');

print('checking is "a" present in the "GMS Grameena Vikas School"  -->  ', 'a' in school_name);
print('checking is "A" present in the "GMS Grameena Vikas School"  -->  ', 'A' in school_name);
print('checking is "a" present not in the "GMS Grameena Vikas School"  -->  ', 'a' not in school_name);
print('checking is "A" present not in the "GMS Grameena Vikas School"  -->  ', 'A' not in school_name);


print_star('Chekcing equality opertor "is" and  "==", "is not", !='); 
    # is operator always compares id of the objects
    # == always compares the content of the objects
text_one = 'Praveen';
text_two = 'Hello';
text_three = 'Praveen';
print(f'{text_one} is {text_two} ? {text_one is text_two}');
print(f'{text_one} == {text_two} ? {text_one == text_two}');

print(f'{text_one} is {text_three} ? {text_one is text_three}');
print(f'{text_one} == {text_three} ? {text_one == text_three}');

print(f'{text_one} is not {text_two} ? {text_one is not text_two}');
print(f'{text_one} != {text_two} ? {text_one != text_two}');

print(f'{text_one} is not {text_three} ? {text_one is not text_three}');
print(f'{text_one} != {text_three} ? {text_one != text_three}');

print_star('Using Relational Operators like (> , >= ,<, <=)');
    # relationl operators compares the ordianl of the each element present in the strings to get the result
text_one = 'Praveen';
text_two = 'Hello';
text_three = 'praveen';
print(f'Ordianal value of "P" --> {ord("P")}');
print(f'Ordianal value of "p" --> {ord("p")}');
print(f'Ordianal value of "H" --> {ord("H")}');

print(f'{text_one} > {text_two} ? {text_one > text_two} ');
print(f'{text_one} > {text_three} ? {text_one > text_three} ');
print(f'{text_two} > {text_three} ? {text_two > text_three} ');

print(f'{text_one} >= {text_two} ? {text_one >= text_two} ');
print(f'{text_one} >= {text_three} ? {text_one >= text_three} ');
print(f'{text_two} >= {text_three} ? {text_two >= text_three} ');

print(f'{text_one} < {text_two} ? {text_one < text_two} ');
print(f'{text_one} < {text_three} ? {text_one < text_three} ');
print(f'{text_two} < {text_three} ? {text_two < text_three} ');

print(f'{text_one} <= {text_two} ? {text_one <= text_two} ');
print(f'{text_one} <= {text_three} ? {text_one <= text_three} ');
print(f'{text_two} <= {text_three} ? {text_two <= text_three} ');

print_star('Using del operator to delete the String object');
text_one = 'Japan';
text_two = text_one;

print(f'String value ---> {text_one}');
print(f'String value ---> {text_two}');

print(f'Before deleting the object {text_one} , number of references : {getrefcount(text_one)}')
del text_one;
print(f'After deleting the object {text_two} , number of references : {getrefcount(text_two)}')
    # Here text_one reference will be deleted not the string object 
# print(text_one); # NameError: name 'text_one' is not defined. Did you mean: 'text_two'?
del text_two; 
print(f'After deleting the object Japan , number of references : {getrefcount("Japan")}')


print_star('Working with string predefine methods');

print(f'removing white spaces of the string from both ends --> " RAM " ( length --> {len(" RAM ")} ) using strip function --> {" RAM ".strip()} with length {len(" RAM ".strip())}');
print(f'removing white spaces of the string from right end --> "RAM " ( length --> {len("RAM ")} ) using rstrip function --> {"RAM ".rstrip()} with length {len("RAM ".rstrip())}');
print(f'removing white spaces of the string from left end --> " RAM" ( length --> {len(" RAM")} ) using lstrip function --> {" RAM".lstrip()} with length {len(" RAM".lstrip())}');

print(f'print length of the string using len()--> " RAM " with lenght {len(" RAM ")}');

print(f'convert string to lowercase using lower() -- "RAM" --> {"RAM".lower()}')
print(f'convert string to uppercase using upper() -- "ram" --> {"ram".upper()}')
print(f'Swap the string case using swapcase() -- "RaM" --> {"RaM".swapcase()}')

print(f'Finding number of occurances of the given char in a string using count() -->  "Hello World" --> searching -> "l" -- count :  {"Hello World".count("l")}' );
print(f'Finding number of occurances of the given char in a string using count() -->  "Hello World" --> searching -> "ld" -- count :  {"Hello World".count("ld")}' );
print(f'Finding number of occurances of the given char in a string using count() -->  "Hello World" --> searching -> "e" -- count :  {"Hello World".count("e")}' );
    # count will return "0" if there is not matching char
print(f'Finding number of occurances of the given char in a string using count() -->  "Hello World" --> searching -> "a" -- count :  {"Hello World".count("a")}' );

print(f'finding the given char available at index using find() --> : "Hello World" --> searching --> "l" --> at index :  {"Hello World".find("l")}');

 # find  will return -1 if the given char is not avaialble in a string
print(f'finding the given char available at index using find() --> : "Hello World" --> searching --> "x" --> at index :  {"Hello World".find("x")}');
print(f'finding the given char available at index using rfind() --> : "Hello World" --> searching --> "l" --> at index :  {"Hello World".rfind("l")}');
    # index  will thorw "ValueError" if the given char is not avaialble in a string
print(f'finding the given char available at index using index() --> : "Hello World" --> searching --> "l" --> at index :  {"Hello World".index("l")}');
# print(f'finding the given char available at index using index() --> : "Hello World" --> searching --> "x" --> at index :  {"Hello World".index("x")}');

print(f'Capitalize the string using capitalize() and title() --> "hello world" --> {"hello world".capitalize()} -- > {"hello world".title()}');



