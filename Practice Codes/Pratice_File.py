class Store:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    
    @staticmethod
    def calc_disc(rs,disc):
        f_price = rs - (disc * rs/100)
        print(f"The Final Price Is {f_price}")
        
s1 = Store("Iphone",85000)
s1.calc_disc(100000,5)

print(s1.name)
print(s1.price)