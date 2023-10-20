class Resturant:
    def __init__(self,name, menu=[]) -> None:
        self.name = name
        self.chef = None
        self.server = None
        self.manager = None
        self.menu = menu
        self.revenue = 0
        self.expense = 0
        self.balance = 0
        self.profit = 0

    def add_employee(self,employee_type, employee):
        if employee_type == 'chef':
            self.chef = employee
        elif employee_type == 'server':
            self.server == employee
        elif employee_type == 'manager':
            self.manager = employee

    def received_payment(self,amount,customer,order):
        if amount >= order.bill :
            self.revenue += order.bill
            self.balance += order.bill
            self.due_amount = 0
            return amount - order.bill
        
    def pay_expense(self,amount,description):
        if amount < self.balance :
            self.expense += amount
            self.balance -= amount
            print(f'Expense {amount} for {description} ')
        else:
            print(f'Not Enough Money To Pay {amount}')

    def pay_salary(self,employee):
        if employee.salary < self.balance :
            employee.received_salary()
