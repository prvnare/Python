# defining a class
class Student:
    def __init__(self) -> None:
        print('constructor');

# creating an object to the class
student = Student();  

class Student:
    # consructor of the class 
    def __init__(self, name, age, className, marks) -> None:
        self.name = name;
        self.age = age;
        self.className = className;
        self.marks =  marks;
        print(f'Student with Name: {self.name}, Age: {self.age}, class:  {self.className} and marks: {self.marks} has created');

# creating an Object of Student class
test = Student('Ram', 10, 3, 98);

class Student:
    # class can have multiple consturctors 
    def __init__(self, a, b) -> None:
        print('constructor with 3 parameters');

    # constructor with 2 parameters
    def __init__(self,a) -> None:
        print('constructor with 2 params');

    # constructor with 2 parameters
    def __init__(self) -> None:
        print('constructor with 1 params');


# creating an Object by using 3 parameter constructor
# student = Student(1,2); #TypeError: Student.__init__() takes 1 positional argument but 3 were given

# creating an Object by using 2 parameter constructor
# student = Student(1); #TypeError: Student.__init__() takes 1 positional argument but 2 were given

# creating an Object by using 1 parameter constructor
student = Student(); 

# overloading concept is not available in python,
# if you define multiple constructors in a class there will not be a compile error but you can create an object with latest constructor only
# in the above example 1 parameter is the latest constructor of the class;


class Student:
    # consructor of the class 
    def __init__(self, name, age, className, marks) -> None:
            # Constuctor is used to initialize the instance variables of a class
        self.name = name;
        self.age = age;
        self.className = className;
        self.marks =  marks;
        print(f'Student with Name: {self.name}, Age: {self.age}, class:  {self.className} and marks: {self.marks} has created');

# creating an Object of Student class and constructor will be invoked by the PVM automatically by creating the object
test = Student('Ram', 10, 3, 98);
print(id(test));
print(type(test));
print(test.age);
# You can call the constructor but wont create an new Object
test = test.__init__(1,2,3,4);  # test will be pointed to NoneType that means if you call the constructor manully PVM wont create new object for the class;
print(id(test));
print(type(test));
# print(test.age); Will be an Error as NoneType wont have age property



class Student:
    # consructor of the class 
    def __init__(self, name, age, className, marks) -> None:
            # Constuctor is used to initialize the instance variables of a class
        self.name = name;
        self.age = age;
        self.className = className;
        self.marks =  marks;
        print(f'Student with Name: {self.name}, Age: {self.age}, class:  {self.className} and marks: {self.marks} has created');
    
    # instance mthod
    def initialize_instanc_variable(self, gender):
        # we can iniitialize instance variables in the instance methods aswell
        self.gender = gender;

    def student_info(self) -> None:
        print(f'Student detaials --> Name: {self.name}, Age: {self.age}, class:  {self.className}, marks: {self.marks} and gender :  {self.gender}');

student = Student('Ram', 10, 5, 95);
# calling instance methods on the object reference
student.initialize_instanc_variable('Male');
student.student_info();


class Student:
    # Static variable available only 1 copy to all the instances of the class
    school_name  = 'GMS Public School';
    def __init__(self) -> None:
        print('Constructor');
    
    @classmethod
    def declaring_static_variable_using_class_method(cls):
        cls.medium = 'Eng';
        Student.address = 'Hyderabad';

print(Student.school_name);
Student.declaring_static_variable_using_class_method();
test = Student();
print(f'student one ref --> {id(test)}');
print('School Name of the student one --> ', test.school_name);
print('School Name of the student one --> ', test.medium);
print('School Name of the student one --> ', test.address);

test = Student();
print(f'student one ref --> {id(test)}');
print('School Name of the student two --> ', test.school_name);
print('School Name of the student two --> ', test.medium);
print('School Name of the student two --> ', test.address);



class Student:
    # Setter 
    def set_name(self, name):
        self.name = name;

    # Getter 
    def get_name(self):
        return self.name;

student = Student();
student.set_name('Naresh');
print(student.get_name());



class Student:
    #static variable
    school_name = 'GMS';
    # Constructor
    def __init__(self, name):
        # instance variable
        self.name = name;
        print('Constructor');

    # Instance method
    def student_info(self):
        print('instance method');

    # class method
    @classmethod
    def school_info(cls):
        print('class method');

    # static method
    @staticmethod
    def school_strength():
        name = 'Ram';
        print('static method');

    # distructor
    def __del__(self):
        print('distructor');


# calling static variable
print(Student.school_name);

#calling static method using class name
Student.school_strength();

#calling class method using class name
Student.school_info();

# creating Object -- using constructor
student = Student('Ram');

# calling  instance varibale using instance
student.student_info();
# calling static method using instance
student.school_strength();
# calling class method using instance
student.school_info()


class Person:
    def __init__(self, name):
        self.name = name;
        print('Person constructor');

class Student(Person):
    def __init__(self, name, age):
        # Calling parent class constructor
        super().__init__(name);
        self.age = age;
        print('Student constructor');
        
student = Student('Ram', 10);
print(student.__dict__);


if __name__ == '__main':
    print("hello world");


class A:
    pass;

class B(A):
    pass;

class C(A):
    pass;

class D(C,B):
    pass;

# finding method resolution order of a class using mro()
print(A.mro());
print(type(A.mro()));
print(A.__mro__);
print(type(A.__mro__));

print(f'B class method reosulution : {B.mro()}');
print(f'B class method reosulution : {B.__mro__}');


print(f'C class method reosulution : {C.mro()}');
print(f'C class method reosulution : {C.__mro__}');


print(f'D class method reosulution : {D.mro()}');
print(f'D class method reosulution : {D.__mro__}');


class X:
    def __init__(self):
        print('Parent constructor');
    
    def m1(self):
        print('Parent class method');

class Y(X):

    def __init__(self):
        print('child constructor');
        super().__init__();
    
    def m1(self):
        print('Child class method');
        super().m1();

y = Y();
y.m1();


class A:
    a = 20;
    def __init__(self, b) -> None:
        self.b = b;


class B(A):
    def __init__(self, b):
        super().__init__(b);
        self.a =60;

    def disp(self):
        print(self.b);
        print(self.a);
        print(super().a);
    

b = B(30);
b.disp();

b.b =40;
b.a =50;
b.disp();


class Book:
    def __init__(self, pages):
        self.pages = pages;
        print('Type ', type(pages));
    

    # magic method for + operator 
    def __add__(self, other_book):
        print('calling magic method');
        return self.pages + other_book.pages;

    def __str__(self) -> str:
        return  str(self.pages);

book_one = Book(10);
book_two = Book(20);
print(book_one + book_two); 

print(book_one);
print(book_two);


# __class__.__name__ --> gives name of the class
class Test:
    def method(self, x):
        print(f'type of the x is : {x.__class__.__name__}');

t = Test();
t.method(10);
t.method(10.3);
t.method(False);
t.method("name");
t.method(10+20j);


# Abstract classes and methods
from abc import (abstractmethod, abstractclassmethod, abstractstaticmethod, ABC);
class Vehicle(ABC):

    @abstractmethod
    def wheels(self):
        pass;

    @abstractstaticmethod
    def color():
        pass;

    @abstractclassmethod
    def gear_type(cls):
        pass;

class Bus(Vehicle):

    def wheels(self):
        return 6;

    @staticmethod
    def color():
        return 'black';

    @classmethod
    def gear_type(cls):
        return 'automatic';

class Auto(Vehicle):
    def wheels(self):
        return 3;

    @staticmethod
    def color():
        return 'Yellow';

    @classmethod
    def gear_type(cls):
        return 'manual';


auto = Auto();
print(auto.wheels());
print(auto.color());
print(auto.gear_type());


bus  = Bus();
print(bus.wheels());
print(bus.gear_type());
print(bus.color());

# vehicle = Vehicle(); TypeError: Can't instantiate abstract class Vehicle with abstract methods color, gear_type, wheels


