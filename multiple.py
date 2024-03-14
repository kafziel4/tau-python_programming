# Parent class 1
class Item:
    def __init__(self, sku):
        self.sku = sku

    def print_sku(self):
        print("The sku is {}.".format(self.sku))


# Parent class 2
class Garment:
    def __init__(self, section, gtype):
        self.section = section
        self.gtype = gtype

    def print_garment(self):
        print("The garment is in section {}, {}.".format(self.section, self.gtype))


# Child class
class Shirts(Item, Garment):
    def __init__(self, sku, section, gtype, name, color):
        self.name = name
        self.color = color
        Item.__init__(self, sku)
        Garment.__init__(self, section, gtype)

    def print_shit(self):
        print("{} {} on sale!".format(self.color, self.name))


blouse = Shirts("00001", 43, "Tops", "Formal Blouse", "White")

blouse.print_sku()
blouse.print_garment()
blouse.print_shit()
