from Menu import Pizza,Burger,Menu,Drinks
from Resturant import Restaurant
from Users import Chef,Customer,Server,Manager
from Order import Order
def main():
   menu = Menu()
   pizza_1= Pizza('Naga pizza',600,'large',['naga','onion'])
   menu.add_menu('pizza',pizza_1)
   pizza_2= Pizza('Cold pizza',700,'small',['ice','onion'])
   menu.add_menu('pizza',pizza_2)
   pizza_3= Pizza('Dal pizza',800,'medium',['dal','onion'])
   menu.add_menu('pizza',pizza_3)

   burger_1 = Burger('Naga Burger',1000,'chicken',['naga','meat'])
   menu.add_menu('burger',burger_1)
   burger_2 = Burger('Beef Burger',3000,'beef',['beef','meat'])
   menu.add_menu('burger',burger_2)


   coke = Drinks('Coke', 50, True)
   menu.add_menu('drinks',coke)
   coffee = Drinks('Coffee', 180, False)
   menu.add_menu('drinks',coffee)


   menu.show_menu()

   restaurant = Restaurant('Near_By_Restaurant',1000,menu)
   
   manager = Manager('Sohana',17,'sohana@gmail.com','natore',3500,'nov 13 2019','core')
   restaurant.add_employee('manager',manager)
   chef = Chef('Akash',17,'akash@gmail.com','pabna',2500,'jan 3 2020','chef','burger')
   restaurant.add_employee('chef',chef)
   server = Server('mohonam',17,'md@gmail.com','tgtrhtr',4000,'dec 1 2020', 'serve')
   restaurant.add_employee('server',server)

   restaurant.show_employees()

   #customer -1
   customer_1 = Customer('Md Akram',1700,56,'akram@gmail.com','dhaka')
   order_1 = Order(customer_1,[pizza_2,coffee])
   customer_1.pay_for_order(order_1)
   restaurant.add_order(order_1)


   #customer -1 paying for order
   restaurant.receive_payment(order_1,5000,customer_1)
   print(restaurant.revenue, restaurant.balance)
   
if __name__== '__main__':
  main() 