class Good(object):
    def __init__(self):
        self.org_price = 1000
        self.discount = 0.7

    @property
    def price(self):
        val = self.org_price * self.discount
        return val

    @price.setter
    def price(self,new_val):
        self.org_price = new_val

    @price.deleter
    def price(self):
        del self.discount

g = Good()

print(g.price)

g.price = 2000
print(g.price)

del g.price
print(g.price)