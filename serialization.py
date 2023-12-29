# Object serialization and deserialization usinf Pickle , JSON and YAML
# Modulue PICKLE is used to serialize/deserialize the object to file vice versa
import pickle;
from random import choice;

# Module JSON is used to serialize/deserialize the object
import json;
import requests;
import jsonpickle;
# defined a Student class
class Student:
    def __init__(self, name, age, gender, grade):
        self.name = name;   
        self.age = age;
        self.gender = gender;
        self.grade = grade;
        self.isMarried = False;
        self.isMinor = True;
        self.haveGF = None;
    def __str__(self):
        return f'{self.name} -- {self.age} -- {self.gender} -- {self.grade} -- {self.isMarried} --{self.isMinor} -- {self.haveGF}';

# Creating an Object for student class
student  = Student('Ram', 10, 'Male', 9);

# serializing the object to file
with open('serialize.txt', 'wb') as file:
    pickle.dump(student, file);


# deserialize the object from the file
with open('serialize.txt','rb') as file:
    student = pickle.load(file);
    print(student.name, student.age, student.gender,student.grade, sep='<--->');

# generator to get number of dummy student objects 
def student_generator(count):
    for i in range(count):
        student_names = ['Ram', 'Raj','Cotton'];
        student_age = [7, 8, 9];
        student_gender = ['Male', 'Female'];
        student_grade = [6, 5, 9];
        yield Student(choice(student_names), choice(student_age), choice(student_gender), choice(student_grade));

list(student_generator(10));

# serializing the list of objects to file
with open('serialize_multiple.txt', 'wb') as file:
    pickle.dump(list(student_generator(10)), file);

# deserialize the list of objects from the file
with open('serialize_multiple.txt','rb') as file:
    student_list = pickle.load(file);
    for student in student_list:
        print(student.name, student.age, student.gender,student.grade, sep=' <---> ');


# Working with JSON serialize and deserialize
student = {'name':'Ram', 'age':10, 'gender':'Male', 'grade': 9, 'isMarried':False, 'isMinor' : True, 'haveBF':None};

# dumps function is used to serialize the dict to json string only --> wont generate any json file 
student_json = json.dumps(student);
print(type(student_json));
print(student_json);

# deserializing the json string to python object using loads function
student_from_json_string  = json.loads(student_json); 
print('string from the json string --> ', student_from_json_string);

# working with  dict with multiple keys and values
student_dict= {};
student_dict["student_one"] = {'name':'Ram', 'age':10, 'gender':'Male', 'grade': 9, 'isMarried':False, 'isMinor' : True, 'haveBF':None};
student_dict["student_two"] = {'name':'Ram', 'age':10, 'gender':'Male', 'grade': 9, 'isMarried':False, 'isMinor' : True, 'haveBF':None};
student_dict["student_three"] = {'name':'Ram', 'age':10, 'gender':'Male', 'grade': 9, 'isMarried':False, 'isMinor' : True, 'haveBF':None};
student_dict["student_four"] = {'name':'Ram', 'age':10, 'gender':'Male', 'grade': 9, 'isMarried':False, 'isMinor' : True, 'haveBF':None};
student_dict["student_five"] = {'name':'Ram', 'age':10, 'gender':'Male', 'grade': 9, 'isMarried':False, 'isMinor' : True, 'haveBF':None};

# dumps function is used to serialize the dict to json string only --> wont generate any json file 
student_json = json.dumps(student_dict, indent=5, sort_keys=True);
print(type(student_json));
print('Json string from the Python dict : ---> ',student_json);

# deserializing using loads()
print('Pthon object from json string --> ', json.loads(student_json), type(json.loads(student_json)));

# serializing to json file 
with open('student.json','w') as file:
    json.dump(student_dict, file, indent=5, sort_keys=True);

# deserializing from file
with open('student.json','r') as file :
    for key, value in json.load(file).items():
        print(key, value);

# deserializing from file
with open('employeeData.json', 'r') as file:
     for key, value in json.load(file).items():
        print(key, value);

# requesting from the API and receving the json 
for item in requests.get('https://api.covidtracking.com/v1/states/info.json').json(): # returns list of dict
    for key, value in item.items(): # returns dict
        print(key, value);

for key,value in requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json().items(): # returns dict directly
    print(key, value);


# serialize/deserialize user defined class objects to json usin jsonpickle module

#serialization as json string
student_list = [student for student in student_generator(10)];
print(student_list);
json_string =jsonpickle.encode(student_list, indent=4);
print(json_string);

# deserializing the json string to Student objcet;
student_list = jsonpickle.decode(json_string);
print(student_list);
for student in student_list:
    print(student);


#serialization student to json file
# its just a normal file IO operation of writing and reading of the json string
student_list = [student for student in student_generator(10)];
print(student_list);
with open('student.json', 'w') as file:
    # Normal file write operation here
    file.write(json_string);
    print('File serializing');

# deserializing the json from file to Student objcet;
with open('student.json','r') as file:
    # Normal file read operation here nothing sepecial
    for student in  jsonpickle.decode(file.read()):
        print(student);

