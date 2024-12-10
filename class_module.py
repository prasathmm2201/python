# class
class Person:
    def __init__(self , name):
        self.name = name
    def get_name(self):
        return f"Hi {self.name}"


class Student(Person):
    def __init__(self, name):
        super().__init__(name)
    def get_name(self , age):
        return f"Hi {self.name} is {age}"
    

# write file
def write_func():
    with open ("text.txt" , "w") as file:
     file.write("Hello, Python!\n")
     file.write("Welcome to file handling.\n")
     file.writelines(["Hello, Python 1!\n" , "Welcome to file handling2 .\n"])
     file.close()
    print("file written")

# read file
def read_file():
    with open("text.txt" , "r") as file:
        constent = file.readlines()
        file.close()
        print(constent)

def read_file():
    with open("text.txt" , "r") as file:
        constent = file.readlines()
        file.close()
        print(constent)

lines = ["line 1" , "line 2" , "line 3"]
# appand
def appand_file():
    with open("text.txt" , "a") as file:
        constent = file.writelines([line + "\n" for line in lines])
        file.close()
        print(constent)

# decorators
def decorator(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper

@decorator
def get_decorator():
    print("all function")


def couter():
    yield print("1")
    yield print("2")
    print("3")
