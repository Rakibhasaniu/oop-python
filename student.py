class Student:
    def __init__(self,name,current_class,id):
        self.name= name
        self.current_class = current_class
        self.id = id
    def __repr__(self) -> str:
        return f'Student with name : {self.name} , class: {self.current_class}, id: {self.id}'
rakib = Student('Rakib Hasan', '4th', '1704005')
print(rakib)