from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self,name,phone,email,address) -> None:
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        
class Customer(User):
    def __init__(self, name,money,phone,email,address) -> None:
        self.wallet = money
        self.__order = None
        super().__init__(name,phone,email,address)

    @property
    def order(self):
        return self.__order
    @order.setter
    def order(self,order):
        self.__order=order
    

    def place_order(self,order):
        self.order = order
        print(f'{self.name} placed an order {order.items}')


    def eat(self,order):
        print(f'{self.name} eating food {order.items}')

    def pay_for_order(self,amount):
        pass

    def give_tips(self,tips_amount):
        pass

    def write_review(self,stars):
        pass



class Employee(User):
    def __init__(self, name, phone, email, address,salary,starting_date,department) -> None:
        super().__init__(name, phone, email, address)
        self.salary = salary
        self.starting_date = starting_date
        self.department = department

class Chef(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, department,cooking_item) -> None:
        super().__init__(name, phone, email, address, salary, starting_date, department)
        self.cooking_item = cooking_item
