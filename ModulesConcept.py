# importing members of FunctionTopic module
import FunctionsTopic;
import math;

# aliasing FunctionsTopic module as ft so that we can use ft.members directly
import FunctionsTopic as ft

# importing specific members of the module
from FunctionsTopic import iseven


print('using members of other modules');
FunctionsTopic.add(10, 20);
print(ft.multiply(2, 4));
print(iseven(10));


print(dir());
for i in dir(math):
    print(i);

print(help(math));

print('1', __doc__);
print('2', __file__);
print('3', __name__);
print('4', ft.__name__);
print('5', __package__);


