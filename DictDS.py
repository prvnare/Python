dictDs = {};
print(type(dictDs));
print(dictDs);

# dictionary creation
dictEx = {};
print(dictEx);
dictEx = {10: 20, 20: 30}
print(dictEx);
dictEx = dict([(1, 2), (2, 3), (4, 5)]);
print(dictEx);
dictEx = dict([[1, 2], [3, 4], [5, 6]]);
print(dictEx);


# adding elements to DICT
dictDs[100] = 'ramu';
print(dictDs);

# accessing elements of DICT

dictEx[1];
# dictEx[100]; ERROR

del dictEx[1];
print(dictEx);

del dictEx[3], dictEx[5];
print(dictEx);

# del dictEx[1]; ERROR
print(dictEx);


# print(dictEx + dictEx); ERROR (+) NOT APPLICABLE
# print(dictEx * 2); ERROR (*) NOT APPLICABLE


dictEx = {1: 2, 3: 4, 5: 6, 7: 9};
print(len(dictEx));

print(dictEx.get(1));
print(dictEx.get(73));
print(dictEx.get(13, 300));

d = {1: 2};
d1 = {3: 4};
d.update(d1);
d.update({1: 4});
print(d);

print(d.keys());
for key in d.keys():
    print(key, end=' ');


print(d.values());
for value in d.values():
    print(value, end=' ');

print(d.items());
for item in d.items():
    print(item, end=' ');

print();

dictEx = {1: 2, 3: 4, 5: 6, 7: 8};
# key = int(input('enter a key to find the value'));
# if key in dictEx:
#     print(f'value for given key is {dictEx[key]}');
# else:
#     print('No key present');

# value = int(input('enter a value to find the key'));
# for k, v in dictEx.items():
#     if v == value:
#         print(f'corresponding key is {k}');
#         break;
# else :
#     print('No key present');

print(d.pop(1));
print(d.pop(1, 3));

print(d);
print(d.setdefault(4, 5));
print(d);
print(d.setdefault(4, 6));
print(d);


