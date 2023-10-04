class Person:
    def __init__(self, name,age,height,weight) -> None:
        self.name=name
        self.age = age
        self.height = height
        self.weight = weight
    def eat(self):
        print("khai")
    def exercise(self):
        raise NotImplementedError
class Cricketer(Person):
    def __init__(self,name,age,height,weight,team) -> None:
        self.team = team
        super().__init__(name,age,height,weight)
        #override
    def eat(self):
        print('Vegetables')
    def exercise(self):
        print('gym kor hala')

    def __add__(self,other):
        return self.age + other.age

sakib= Cricketer('sakib',45,68,123,'bangladesh')
# print(sakib.__dict__)
# sakib.eat()
# sakib.exercise()
mushi = Cricketer('Mushi',36,34,123,'Bd')

#plus sign overload
print(45+63)
print('sakib' + 'rakib')
print([12,98]+[5,6,7,1,2])
print(sakib + mushi)