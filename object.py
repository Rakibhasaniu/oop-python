class Person:
    def __init__(self, name,age):
        self.name = name 
        self.age = age
        print(name)
        print(age)
       

    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    
a_person = Person("Rakib Hasan",5)
b_person = Person("Sohana Shitol",45)
print(a_person.get_name())
print(b_person.get_name())
print(b_person.get_age())
print(a_person.get_age())