from Menu import Pizza,Burger,Menu,Drinks
from Resturant import Resturant
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

   restaurant = Resturant('Near_By_Restaurant',1000,menu)
   
   
if __name__== '__main__':
  main() 