# **************
# IDENTIFIERS
# **************

####
#
# a-z, A-Z 0-9 and _ are allowed chars
# Reserved words are not allowed
# Case Sensitive language
# a and A is not the same
#
####

name = 'Praveen';   # valid

# 123 = '10' ;      # invalid it should not start with numbers

name123 = 0;        # valid, identifier can contain numbers

# if = 20 ;         # invalid , reserved words not allowed

name_ = 123         # Valid

# name% = 123       # Invalid, % is not allowed as identifier

normalVariable = 'Normal variable declaration';
_protectedVariable = 'Protected variable declaration in python';
__privateVariable = 'Private variable declaration';
__magicVariable__ = 'Language specific variable declaration , wont be used frequently in day to day programs';


# **************
# RESERVED WORDS or KEY WORDS in Python
# **************

#####
#
#
# Total 35 key-words are available in Python
#
#  True, False, None
#  and, or, not,
#  if, elif, else
#  while, for, break, continue, in, return, yield
#  try, except, raise, finally, assert
#  import, from, as, class, def, pass
#  global, nonlocal, lambda, del, with
#
#  async, await  # Added newly
#
#  import keyword
#  print(keyword.kwlist);
#####


# **************
# DATA TYPES
# **************

#####
#
# Dynamically typed language
#
# no need to specify type explicitly to hold the value in variables
#
#
#  *************   EVERYTHING IN PYTHON IS OBJECT   *************
#
# Types :
#            1) int
#            2) float
#            3) complex
#            4) str
#            5) bool
#            6) list
#            7) tuple
#            8) set
#            9) frozenset
#            10) dict
#            11) bytes
#            12) bytearray
#            13) range
#            14) None
#
#
#####
variable = None;
print(id(variable));
variable = 'Holds string type --> and not specifying any type for variable ';

# type() --> used to get the type of the variable
# id() --> used to get the memory address of the object

print(type(variable));
print(id(variable));

print('********************');
variable = 10;
tempVariable = 10;  # Observation uses the same object (10)
print('variable Id', id(variable));
print('tempVariable Id', id(tempVariable));
print('is variable same as variable : ', variable is variable);     # True
print('is variable and tempVariable are same : ', variable is tempVariable);  # True  --> as it uses the same object

print('********************');
tempVariable = tempVariable + 10;
print('variable Id', id(variable));
print('tempVariable Id', id(tempVariable));
print('value of variable : ', variable);
print('value of tempVariable : ', tempVariable);
print('is variable and tempVariable are same : ', variable is tempVariable);
print('********************');

print('********************');
tempVariable = variable;
print('variable Id', id(variable));
print('tempVariable Id', id(tempVariable));
variable = variable + 20;
print('variable Id', id(variable));
print('tempVariable Id', id(tempVariable));
print('value of variable : ', variable);
print('value of tempVariable : ', tempVariable);
print('is variable and tempVariable are same : ', variable is tempVariable);
print('********************');


# **************
# DATA TYPE :  1) INTEGRAL DATA TYPE (WHOLE NUMBERS)  INT
#
#
#   represented in 4 ways
#                           1) Binary form  ---> 0b or 0B
#                           2) Octal from   --> 0O or 0o
#                           3) Decimal form --> Default
#                           4) HexaDecimal  form --> OX or Ox
#
# **************


print('********************');
intType = 10;
print(type(intType));
intType = 100000000000900909090900900990;  # there is no type called LONG in python 3 , Python 2 was having Long type
print(type(intType));
print('********************');

# Binary Form   only 0 and 1 is allowed
print('*********  BINARY FORM  ***********');
binaryForm = 0B1010;
print(binaryForm);
print(type(binaryForm));

binaryForm = 0b101010;
print(binaryForm);
print(type(binaryForm));
print('********************');


# OCTAL Form   only 0 to 7 is allowed
print('*********  OCTAL FORM  ***********');
octalForm = 0O1010;
print(octalForm);
print(type(octalForm));

octalForm = 0o101010;
print(octalForm);
print(type(octalForm));
print('********************');


# DECIMAL Form   only 0 to 9  is allowed
print('*********  DECIMAL FORM  ***********');
decimalForm = 1010;
print(decimalForm);
print(type(decimalForm));

decimalForm = 101010;
print(decimalForm);
print(type(decimalForm));
print('********************');


# HEXA-DECIMAL Form   only 0 to 9 and A,B,C,D,E,F is allowed
print('*********  HEXA-DECIMAL FORM  ***********');
hexaDecimalForm = 0X1010;
print(hexaDecimalForm);
print(type(hexaDecimalForm));

hexaDecimalForm = 0xFACE;
print(hexaDecimalForm);
print(type(hexaDecimalForm));
print('********************');

binaryForm = 0B01;
print(binaryForm);


# **************
# DATA TYPE :  2) FLOAT DATA TYPE  FLOAT
# **************

floatingValue = 123.89;
print(type(floatingValue));
exponentialForm = 1.2E3;
print(type(exponentialForm));
print(exponentialForm);
print('********************');

# **************
# DATA TYPE :  3) COMPLEX DATA TYPE  A+Bj; (J/j is mandatory)
# Where 'A' is real part
# and 'B' is imaginary part
# and j*j = -1
# and j = root of -1
# Not required to focus on this as we are not using much in our day to day programming
# **************


complexNumber = -10.4 + -20.7j;
print(type(complexNumber));
print(complexNumber.real);
print(complexNumber.imag);
print('********************');

# **************
# DATA TYPE :  4) BOOL DATA TYPE  Boolean
# Accepted is True and False (Capital T and F)
# **************

booleanValue = True;
print(type(booleanValue));
print(booleanValue);

temp = 10;
temp2 = 20;
tempBoolean = 10 > 20;
print(tempBoolean);
print(type(tempBoolean));

# Arithmatic Operations on boolean
# True  = 1
# False = 0
print(True + True);
print(True - False);
print(True * False);
print('********************');

# **************
# DATA TYPE :  5) STRING DATA TYPE  str
# 'X',"X",'''X''',"""X"""
# **************
stringValue = 'String Data Type';
print(stringValue);
print(type(stringValue));
singleQuoteValue = 'single quoted value';
print(singleQuoteValue);
doubleQuotedValue = "Double quoted value";
print(doubleQuotedValue);
tripleQuotedValue = ''' Triple
                        Quoted
                        Value''';
print(tripleQuotedValue);
doubleQuotesInSingleQuotedString = 'This is an example for using "double Quotes in single quoted literal" value';
print(doubleQuotesInSingleQuotedString);
singleQuotesInDoubleQuotedStringLiteral = " 'Example to use single quoted literal in double quotes' ";
print(singleQuotesInDoubleQuotedStringLiteral);
singleQuotesAndDoubleQuotesInTripleQuotes = ''' example value 'single' and "double" quotes in triple quotes''';
print(singleQuotesAndDoubleQuotesInTripleQuotes);

# String index starts from "0"   (forward) and "-1" for last index (Reverse)
print('********************');
stringValue = 'Praveen';
print(stringValue[0]);
print(stringValue[1]);
print(stringValue[2]);
print(stringValue[6]);
print(stringValue[-1]);  # Valid
print(stringValue[-7]);  # Valid


# **************
# TYPE CASTING:
# **************

print('********************');
# int() --> converting from other types to int
print('Float : ', int(10.09));  # from float to int
print('Boolean : ', int(True));
print('Boolean : ', int(False));
print('String : ', int('10'));  # Should be only in integral value with base 10. Floating is not allowed here
# print(int(10+10j));  ERROR  Cannot covert Complex to int type

print('********************');
print('Integer: ', float(10));
print('Integer: ', float(0XFACE));
# print(float(10+10j));  ERROR  Cannot covert Complex to float type
print('Boolean : ', float(True));
print('Boolean : ', float(False));
print('String : ', float('10'));
print('String : ', float('10.23'));

print('********************');
print(complex(10));
print(complex(10j));
print(complex(10.10));
print(complex(10.10j));
print(complex(True));
print(complex(False));
print(complex('10'));
print(complex('10.23'));
print(complex(10, 20));
print(complex(10.90, 20.98));
# print(complex(10.90,"20.98" ));  # ERROR
# print(complex("10.90","20.98" ));  # ERROR
# print(complex('0XFACE'));

print('********************');
print('Integer : ', bool(10));  # if value is 0 then only it is False else it is True
print('Integer : ', bool(0));   # False
print('Integer : ', bool(-1));  # True

print('Float : ', bool(10.09));  # True
print('Float : ', bool(0.0));  # False
print('Float : ', bool(0.1));  # True

print('Complex : ', bool(10+4J));  # True
print('Complex : ', bool(0+0J));  # False

print('String : ', bool(''));  # if the argument is empty then only it considered as False otherwise it is True
print('String : ', bool('ABC'));  # True
print('String : ', bool('Yes'));  # True
print('String : ', bool('No'));  # True
print('String : ', bool('true'));  # True
print('String : ', bool('false'));  # True


print('********************');
print('Integer: ', str(10));
print('Float : ', str(10.0));
print('Boolean:', str(True));
print('Boolean:', str(False));
print('Complex:', str(10+4j));
print('********************');

# **************
# DATA TYPE :  6) LIST DATA TYPE
#
# Order is preserved
# Duplicates allowed
# Represented  --> []
# **************
print('********************');

listType = [1, 2, 3, 5, 6, 6, 5, 4, 3, 2, 1, True, False, 'Text'];   # LIST TYPE with Duplicates

print(type(listType));
print(listType);

print(listType[0]);
print(listType[-1]);
print(listType[0:5]);   # Slicing can be applied

emptyList = [];
emptyList.append(1);  # Adding elements to List
emptyList.append(2);
emptyList.append(23);
emptyList.append(25);
emptyList.append(2);
emptyList.append(26);
emptyList.append(2);

print(emptyList);

emptyList.remove(2);  # First occurrence of the element will be removed from the starting index
print(emptyList);

emptyList[5] = 27;
print(emptyList);

print('********************');


# **************
# DATA TYPE :  6) TUPLE DATA TYPE
#
# Order is preserved
# Duplicates allowed
# Represented  --> ()
# IMMUTABLE --> Adding removing of elements is not allowed
# **************
print('********************');

tupleType = (1, 2, 3, 4, 5, 'a', 'b', True, False);

print(type(tupleType));
print(tupleType);

#  tupleType.append(1);  ## NOT ALLOWED
#  tupleType.remove(1);  ## NOT ALLOWED
#  tupleType[1] = 123;

print(tupleType[1]);
print(tupleType[-1]);
print(tupleType[1:5]);

print(type(('a')));  # String type
print(type((False)));  # Boolean
print(type((1)));  # Int
print(type(()));  # EMPTY Tuple


print(type(('a',)));  # Tuple  single valued tuple should end with ","
print(type((False,)));  # Tuple
print(type((1,)));  # Tuple
print(type(()));  # EMPTY Tuple


# **************
# DATA TYPE :  6) SET DATA TYPE
#
# Order is not preserved
# Duplicates not allowed
# Represented with ---> {}
# MUTABLE --> Adding removing of elements is  allowed
# **************
print('********************');
setType = {0, 1, 2, 3, 4, 4, 3, 2, True, True, False, False, 1, 0, 0};  # Duplicates removed
# BIT STRANGE -- True and False are considering as 1 and 0 here
print(setType);
print(type(setType));
# print(type[0]);  # Indexing is not allowed : ERROR
print(type({}));  # Dict type
print(type(set()));  # Empty Set


# **************
# DATA TYPE :  6) FROZENSET DATA TYPE
#
# Order is not preserved
# Duplicates not allowed
# Represented with ---> {}
# IMMUTABLE --> Adding removing of elements is not  allowed
# **************
print('********************');

setType = {1, 3, 4, 2, 3, 1};
frozensetType = frozenset(setType);
print(type(frozensetType));
print(frozensetType);  # frozenset({1, 2, 3, 4})

# **************
# DATA TYPE :  6) DICT DATA TYPE
#
# Key value pair representation
# Order is not preserved
# Duplicates keys will be allowed but value will overriden by new key value
# Represented with ---> {}
# MUTABLE --> Adding removing of elements is allowed
# **************
print('********************');

dictType = {'k1': 'v1', 'k2': 'v2'};  # Dictionary representation
print(type(dictType));
print(dictType);

dictType['k3'] = 'v3';
dictType['k4'] = 'v4';
dictType['k1'] = 'v';  # Duplicates keys will be allowed but value will overriden by new key value
print(dictType);
print('********************');

# **************
# DATA TYPE :  6) RANGE DATA TYPE
#
# Represents sequence of numbers
# Immutable
# Indexing and slicing is applicable
# **************
print('********************');

rangeType = range(10);  # Creation Type 1
print(type(rangeType));
print(rangeType);

for value in rangeType:
    print(value);

rangeType = range(3, 7);  # Creation Type 2
print(type(rangeType));
print(rangeType);
for value in rangeType:
    print(value);

rangeType = range(False);
print(rangeType);
print(type(rangeType));
for value in rangeType:
    print(value);
print('********************');

# **************
# DATA TYPE :  6) BYTES DATA TYPE
# Only allowed integers from 0 to 255 values
# Immutable
# Slicing and indexing is applicable
# **************
print('********************');
# bytesType = bytes(listType);  # String type cannot be converted to bytes
bytesType = bytes([1, 3, 4]);   # Allowed integer values from 0 to 255
print(type(bytesType));
print(bytesType);
for value in bytesType:
    print(value);

# bytesType = bytes([1, 1.4, 1.3, 2])  # Floating values are not allowed
print(type(bytesType));
print(bytesType);
for value in bytesType:
    print(value);

print(bytesType[1]);   # Index allowed
print(bytesType[:2]);  # Slice is allowed
print(bytesType[-1]);  # Index in reverse
# bytesType[1] = 123;   # ERROR : Immutable
print('********************');

# **************
# DATA TYPE :  6) BYTEARRAY DATA TYPE
# Only allowed integers from 0 to 255 values
# mutable
# Slicing and indexing is applicable
# **************

# SAME AS BYTES --> ONLY DIFF IS MUTABLE

byteArrayType = bytearray([1, 2, 3, 5]);
print(type(byteArrayType));
for value in byteArrayType:
    print(value);

byteArrayType[1] = 20;
print(type(byteArrayType));
for value in byteArrayType:
    print(value);


# OPERATORS
# ARITHMATIC OPERATOR:
# +, -, *, **(Exponential), /, //(floor division), %

print(1+2);
print(1-2);
print(1*2);
print(10%2);


print('a' + 'b');  # ab
# print('a' * 'b');
# print(10 + 'a');  # Error
print(2 * 'w');   # ww
# print(2.0 * 'w');   # TypeError: can't multiply sequence by non-int of type 'float'



print(10/2);  # Division always gives result in floating values
print(10//2);  # // will give the result in near to floor value
print(10//0.2);  # 49.0
# print(10/0);  # ZeroDivisionError: division by zero
# print(10.0/0); # ZeroDivisionError: division by zero
# print(10//0);  ZeroDivisionError: division by zero
# print(10.0/0); ZeroDivisionError: division by zero
print(0/1);
print(0/1);
print(0/1.0);
print(0//1);
print(0//1.0);


print(2**2);  # ** is exponential value
print(4**2);  # (a**b) --> a power of b
print('********************');

# Relational Operators
print('********************');
# print(10+4j > 10+2j);
print(10>10);
print(10>10.1);
print(10.2>10.1);
# print(10.2 > '10.1');
print('10' > '10aaaa');
print('********************');

# Equality Operators
print('********************');
# == and !=
print(10 == 20);
print(10 != 20);
print(10 == 10.0);
print('a' == "a");
print(True == 1);
print(20+10j == 10+20j);
print('********************');

# Logical Operators for non-boolean values

print('********************');
print('a' and 'b');  # b
print(10 and 0);  # 0
print(0 and 10);   # 0
print('' and 'a');  # ''
print([] and {});  # []
print((1,) and frozenset());  # frozenset
print('********************');
print(0 or 1);  # 1
print('' or 1);     # 1
print('a' or 0);    # a
print('a' or '');   # a
print([] or 'abc');     # abc
print([1, 2] or {});    # [1, 2]

# Ternary Operator
print('********************');
valueOne = 10;
valueTwo = 20;
# Semantic --> TrueValue if condition else falseValue
valueThree = 30 if valueOne > valueTwo else 40;
print(valueThree);
 







