stringValue = 'Name';
print(type(stringValue), stringValue);

# Declaring string in single quotes
singleQuotedString = 'SingleQuotedValue';
print(type(singleQuotedString), singleQuotedString);

# Declaring string in double quotes
doubleQuotedString = "Double quoted value";
print(type(doubleQuotedString), doubleQuotedString);

# Declaring string in triple quotes
tripleQuotedString = """Triple quoted value
                        in multiple lines""";
print(type(tripleQuotedString), tripleQuotedString);

print(stringValue[0])
print(stringValue[-1])
# print(stringValue[-100])

# Program to display +ve and -ve index of a character in a string

# input_value = input('Enter a string');
#
# positiveIndex = 0;
# while len(input_value) > positiveIndex:
#     print('The character present at +ve index : {} is {}'.format(positiveIndex, input_value[positiveIndex]));
#     print('The character present at -ve index : {} is {}'
#           .format(positiveIndex-len(input_value), input_value[positiveIndex - len(input_value)]));
#     positiveIndex = positiveIndex + 1;


name = 'Praveen';
print(name[2:5]);   # ave
print(name[:5]);    # Pravee
print(name[2:]);    # aveen
print(name[:]);     # Praveen
print(name[::2])    # Paen
print(name[2:5][:4:2])  # Slicing on slicing output


# Case study
sampleValue = 'abcdefghij';
print(sampleValue[1:6:2]);  # bdf
print(sampleValue[::1]);    # abcdefghij
print(sampleValue[::-1]);   # jihgfedcba

# Mathematical Operators;
#   + operator
print('First' + 'Name');
# print('First' + 10);  # Error

#   * operator
print('First' * 2);
# print('First' + '10');  # Error

# MemberShip operator
# in
# not in

print('a' in name);
print("A" in name);

print('a' not in name);
print("A" not in name);
dir(str);


# predefined methods of the string

print("  123".lstrip());
print("123  ".rstrip());
print("  123  ".strip());

print('typing is so interesting'.find('is'));
print('typing is so interesting'.find('is', 8));
print('typing is so interesting'.find('in', 8, 15));

print('typing is so interesting'.rfind('in'));
print('typing is so interesting'.rfind('is', 8));
print('typing is so interesting'.rfind('in', 1, 8));
print('typing is so interesting'.rfind('in', 8, 1));


# stringValue = input("enter a string").strip();
# subString = input("substring to identify").strip();
#
# repetitionFlag = stringValue.find(subString);
# if repetitionFlag == -1:
#     print('No substring is available');
# count = 1;
# while repetitionFlag != -1:
#     repetitionFlag = stringValue.find(subString, repetitionFlag + len(subString), len(stringValue));
#     if repetitionFlag != -1:
#         count = count + 1;
#
# print(count);



