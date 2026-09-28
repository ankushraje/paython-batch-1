# proprties


class Product:
    def __init__(self, price):
        self.price
        #self.set_price(price)

    # self.price = price
    
    #@classmethod # conver a instance method to class method
    @property
    def price(self):#==> get_price
        return self.__price

    @price.setter
    def set_price(self, value):
        if value < 0:
            raise ValueError("Price can not be negative")
        self.__price = value

    #price = property(get_price, set_price)


product = Product(50)
print(product.price)