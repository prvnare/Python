def key_generator():
    yield 'a';
    yield 'b';
    yield 'c';

generator = key_generator();
print(type(generator));

while True:
    try:
        value = next(generator);
        print(value);
    except: 
        break;

# no need to catch exception
for x in generator:
    print(x);


def getNvalues(n):
    for i in range(1,n):
        yield i;

for i in getNvalues(10):
    print(i);


def get_febonacci_series(n):
    start = 0;
    next = 1;
    for i in range(n):
        yield start; 
        start, next = next, start+next;
        

for i in get_febonacci_series(7):
    print(i, end='--');
print();

