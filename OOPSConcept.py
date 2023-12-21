# Defining a class
class Car:
    """ this is a sample car class to define car functionalities"""
    # properties of the class are defined using variables
    engine = '4 stroke engine';
    color = 'Red colored car';

    # actions of the car defined using the functions

print(Car.__doc__);

class Student:

    def __init__(self, name, age, gender, roll_number):
        print('Parameterized  constuctor');
        print(id(self));
        self.name = name;
        self.age = age;
        self.gender = gender;
        self.roll_number = roll_number;
    
    # def __init__(self):
    #     print('Default constuctor');
    #     self.name = "name";
    #     self.age = "age";
    #     self.gender = "gender";
    #     self.roll_number = "roll_number";

    def student_info(self):
        
        print(self.name);
        print(self.age);
        print(self.gender);
        print(self.roll_number);

# student = Student();

# print(student.age);
# print(student.name);
# print(student.gender);
# print(student.roll_number);


student = Student('Ram', 30, 'Male', 101);

print(id(student));
print(student.age);
print(student.name);
print(student.gender);
print(student.roll_number);
student.student_info(); # Not passing any self variable here as python going to take care of it



class Test:
    def __init__(self):
        print('This is a constructor call');
        print(self);
        print(type(self));

    def info(self, value):
        print('this is an instance method which is taking a parameter as input : {}'.format(value))


test = Test();
test.info(10);


class TemporaryClass:
    def __init__(self):
        print('this is a constuctor');


t = TemporaryClass();
t = TemporaryClass();
t = TemporaryClass();


class UseOfConstructor:
    def __init__(self, a, b, c):
        self.a = a;
        self.b = b;
        self.c = c;
        print('constructor', self.a , self.b, self.c);

t = UseOfConstructor(1, 2, 3);
t = UseOfConstructor(12, 22, 32);
t = UseOfConstructor(21, 22, 23);



class DefaultConstuctor:
    def method(self):
        print('class without constructor');

d = DefaultConstuctor();
d.method();



class Movie:
    production_line = 'ANR Production house';

    def __init__(self, name, producer):
        self.name = name;
        self.producer = producer;

    def getMovieInfo(self):
        print(self.name);
        print(self.producer);

    @classmethod
    def getProductionLine(cls):
        return cls.production_line;

    @staticmethod
    def productionLineAddress():
        return 'Hyderabad';


# calling class method
print(Movie.getProductionLine());

# calling static method
print(Movie.productionLineAddress());

# calling instance methods
movie = Movie('New Movie', 'New Producer');
movie.getMovieInfo();



class Test:
    def __init__(self):
        # initializing instance varibale through constuctor
        self.a = 20;
        self.b = 30;

    def instance(self):
        # initializing instance variable through instance method 
        self.d = 40;
    
    def removeInstances(self):
        # deleting an instance variable
        del self.d;

test = Test();
# prints the instance variable details associated with an object
print(test.__dict__);
# initializing instance variable out side of the class
test.c = 30;
print(test.__dict__);
test.instance();
print(test.__dict__);

for k, v in test.__dict__.items():
    print(k, v);

test.removeInstances();
print(test.__dict__);

# deleting an instance variable
del test.c;
print(test.__dict__);

 # test.removeInstances();  ERROR as d instance variable is not available
print(test.__dict__);


class Test:
    sample = 20;


print(Test.__dict__);
print(Test.__dict__.get('sample'));


# Static variables of the class
class Test:
    # static variable initialization
    a = 10;
    
    def __init__(self):
        self.b  = 20;
        self.a = 50;
        # static variable initialization
        Test.c = 30;
        print(self.a, Test.a);
        # accessing static variable
        print(self.a, self.c, Test.a, Test.c);

    @staticmethod
    def static_method():
        # static variable initializing
        Test.d = 40;
        
        # Accessing static variable
        print(Test.d);

    @classmethod
    def class_method(cls):
        # static variable initializing
        cls.e = 40;
        Test.f = 70;

        # accessing static variabels
        print(cls.e, cls.f, Test.e, Test.f);


    @staticmethod
    def remove_static_variable_with_static_method():
        del Test.d;

    @classmethod
    def remove_static_variable_with_class_method(cls):
        del Test.f, cls.e;

test = Test();
print("with constuctor : ", Test.__dict__);

Test.static_method();
print("with static method : ", Test.__dict__);

Test.class_method();
print("with class method : ", Test.__dict__);

# static variable initialization
Test.g = 90;
print(Test.g, test.g);

# removing static variables

Test.remove_static_variable_with_class_method();
print('after removing the static variable using class method : ', Test.__dict__);

Test.remove_static_variable_with_static_method();
print('removing the static variable using static methos', Test.__dict__)


