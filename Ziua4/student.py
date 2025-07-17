class Student:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def __str__(self):
        return f"Studentul cu numele { self.name} are {self.age}"