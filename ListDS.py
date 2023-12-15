listObject = [];
print(listObject);

listObject.append(1);
listObject.append('123');
listObject.append('Hello world');

print(listObject);

listObject[1] = 'mic check';
print(listObject);


# Ways to create list collection object

l1 = [];
print(type(l1));
print(l1);

l1 = [1, 3, 4];
print(type(l1));
print(l1);

l1 = list('hello_world');
print(type(l1));
print(l1);

# l1 = eval(input('enter list values'));
# print(type(l1));
# print(l1);

print('xyz'.split('y'));

listObject = 'praveen';
print(listObject[2]);
print(listObject[-2]);
# print(listObject[200]);  ## INDEX ERROR
# print(listObject[-20]);  ## INDEX ERROR


print("1 -->", listObject[0:]);
print("2 -->", listObject[0:200]);
print("3 -->", listObject[0:200:2]);
print("4 -->", listObject[0:200:-2]);
print("5 -->", listObject[100::-2]);
print("6 -->", listObject[::-2]);
print("7 -->", listObject[::-1]);
print("8 -->", listObject[-10:-20:-1]);
print("9 -->", listObject[-10:-20]);
print("10 -->", listObject[7:1:-1]);
print("11 -->", listObject[7:2:-1]);
# print("12 -->", listObject[7:2:0]);  ## ValueError: slice step cannot be zero

print("concat", [1, 2] + [3, 4]);
print("repeat", [2, 4] * 3);
print("repeat", [2, '4'] * 3);

print('==', ['1', 2, 3] == [3, 2, '1']);
print('==', ['1', 2, 3] == ['1', 2, 3]);
print('==', ['1', 2, 3] == ['1', 3, 2]);

print(">", ['ram'] > ['raj'])
print(">=", ['ram'] >= ['raj'])
print("<", ['ram'] < ['raj'])
print("<=", ['ram'] <= ['raj'])
print("is", ['ram'] is ['raj']);
print("is not", ['ram'] is not ['raj']);

print('length of the List -->', len(listObject));
print('count -->', listObject.count('a'));
print('index -->', listObject.index('e'));
# print(listObject.index('e1'));

l1 = [];
l1.insert(-10, 30);
l1.insert(10, 930);
print(l1);

print(list(range(1, 11)));
print(range(1, 11));

# List comprehension

print([x for x in range(1, 11)]);
print([x+1 for x in range(1, 11)]);
print([x+'1' for x in 'abcdef']);
print('crating a list of square values', [x*x for x in range(1, 11)])
print('crating a list of square values', [x**2 for x in range(1, 11)])
print('crating a list using comprehension', [x for x in range(1, 11) if x % 2 == 0])

# Examples on list comprehension

numbers = [i for i in range(1, 100)];
print(numbers);

numbers = [i for i in range(1, 100) if '6' in str(i)]
print(numbers);

numbers = 'Hello world welcome to python programming';
print(len([i for i in numbers if i == ' ']));


listObject  = [1, 2, 0, 20, 11, 9, 8];
listObject.sort();
print(listObject);
listOne = ['1', '12', '3244a', 'b'];
listOne.sort();
print(listOne);

listOne = ['c', 'd', 'a', 'b'];
listOne.sort();
print(listOne);

listOne = ['c1', '1d', 'a', 'b'];
listOne.sort();
print(listOne);


listOne = ['*c1', '&1&d', '(a)', 'b'];
listOne.sort();
print(listOne);
