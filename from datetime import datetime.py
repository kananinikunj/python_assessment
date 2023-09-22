from datetime import datetime

class Manager:

    stock = {}

    @classmethod
    def add_stock(cls,name,qty,price):
        if name not in cls.stock:
            cls.stock.update({name : {'qty':qty, 'price':price}})

        else:
            qty = cls.stock[name]['qty'] + qty
            price = (cls.stock[name]['price'] + price) / 2
            cls.stock.update({name : {'qty':qty, 'price':price}})

        with open('fruit_stocks.log','a') as file:
            file.write(f'[{datetime.now()}] -- Stocks Added : (Name : {name} , qty : {qty}, price : {price}) \n')

    @classmethod
    def view_stock(cls):
        with open('fruit_stocks.log','a') as file:
            file.write(f'[{datetime.now()}] -- Stocks Viewed : by Manager ----------------- \n')
        return cls.stock
    

def blank(num):
    for i in range(num):
        print()