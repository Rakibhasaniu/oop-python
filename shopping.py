class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []
    def add_to_cart(self,item,price,quantity):
        product = {
            'item': item,
            'price': price,
            'quantity': quantity
        }
        self.cart.append(product)
    def checkout(self,amount):
        total = 0
        for item in self.cart:
                    #    print("Item:",item['item'],"Price",item["price"],"Quantity:",item["quantity"])
                       total = total + item['price'] * item['quantity']
        print(total)

rakib = Shopping('Rakib Hasan')
rakib.add_to_cart('ciggarate',50,8)
rakib.add_to_cart('alu',90,4)
rakib.add_to_cart('peyaj',20,8)
print(rakib.cart)
rakib.checkout(900)
