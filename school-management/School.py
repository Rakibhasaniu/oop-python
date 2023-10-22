class School:
    def __init__(self,name,address) -> None:
        self.name=name
        self.address = address
        #composition
        self.classrooms = {}

    def add_classroom(self,classroom):
        self.classrooms[classroom.name] = classroom
        
    def student_admission(self,student,classroom_name):
        if classroom_name in self.classrooms:
            self.classrooms[classroom_name].add_Student(student)