class car:

    def __init__(self, colour, price, engine = "v8"):
        self.colour = colour
        self.price = price
        self.engine = engine

    def print_price(self):
        print(self.price)

    def print_colour(self):
        print(self.colour)




mercedes = car("red", 1000, "v6")
bmw = car("black", 1200, "v8")

mercedes.print_price()
bmw.print_colour()
bmw.print_price()





