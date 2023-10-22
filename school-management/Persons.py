import random
class Person:
    def __init__(self,name) -> None:
        self.name = name
    


class Teacher(Person):
    def __init__(self, name,subject) -> None:
        super().__init__(name)
        self.subject = subject

    def teach(self):
        pass

    def take_exam(self,subject,students):
        for student in students:
            marks = random.randint(1,100)
            #TODO: set marks for the subject for each student

class Student(Person):
    def __init__(self, name) -> None:
        super().__init__(name)