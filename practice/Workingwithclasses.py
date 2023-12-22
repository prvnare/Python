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