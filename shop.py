class Shop:
    cart=[]
    def __init__(self, buyer):
        self.buyer= buyer

    def add_to_cart(self,item):
        self.cart.append(item)
rakib = Shop('article')
rakib.add_to_cart('shoes')
rakib.add_to_cart('phone')

print(rakib.cart)
