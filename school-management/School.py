class School:
    def __init__(self,name,address) -> None:
        self.name=name
        self.address = address
        self.teacher =[]
        #composition
        self.classrooms = {}

    def add_classroom(self,classroom):
        self.classrooms[classroom.name] = classroom

    def add_teacher(self,subject,teacher):
        self.teachers[subject] = teacher 
   
        
    def student_admission(self,student,classroom_name):
        if classroom_name in self.classrooms:
            self.classrooms[classroom_name].add_Student(student)
        else:
            print(f'no classroom as named{classroom_name }')

class ClassRoom:
    def __init__(self, name) -> None:
        self.name = name
        #composition
        self.students = []
    
    def add_Student(self,student):
        serial_id = f'{self.name}-{len(self.students)+1} '
        self.students.append(student)

    def __str__(self) -> str:
        return f"Class Room {self.name}: Total Student {len(self.students)}"

    #TODO: sort student by grade
    def got_top_students(self):
        pass