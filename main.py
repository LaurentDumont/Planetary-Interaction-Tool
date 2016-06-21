import sqlite3
import os

class Resource:
    name = ""
    price_buy = 0
    price_sell = 0
    pi_level = ""
    type_id = ""

    def __init__(self, name, pi_level, price_buy, price_sell, type_id):
        self.name = name
        self.pi_level = pi_level
        self.price_buy = price_buy
        self.price_sell = price_sell
        self.type_id = type_id

    def set_price_buy(self, price_buy):
        self.price_buy = price_buy

    def set_price_sell(self, price_sell):
        self.price_sell = price_sell

def planetary_interaction_resources():
    db_file = "pi.db"
    os.remove(db_file)


    file = open("pi.db", 'a')
    file.close()

    conn = sqlite3.connect("pi.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS `resource`
      (name TEXT, pi_level TEXT, price_buy FLOAT, price_sell FLOAT, type_id INTEGER)''')

    global P0_resource
    P0_resource = [Resource("Aqueous Liquids", "P0", 0, 0, 2268),Resource("Autotrophs", "P0", 0, 0, 2305),
                   Resource("Carbon Compounds", "P0", 0, 0, 2267),Resource("Complex Organisms", "P0", 0, 0, 2287),
                   Resource("Felsic Magma", "P0", 0, 0, 2307), Resource("Heavy Metals", "P0", 0, 0, 2272),
                   Resource("Ionic Solutions", "P0", 0, 0, 2309), Resource("Micro Organisms", "P0", 0, 0, 2073),
                   Resource("Noble Gas", "P0", 0, 0, 2310), Resource("Noble Metals", "P0", 0, 0, 2270),
                   Resource("Non-CS Crystals", "P0", 0, 0, 2306), Resource("Planktic Colonies", "P0", 0, 0, 2286),
                   Resource("Reactive Gas", "P0", 0, 0, 2311), Resource("Suspended Plasma", "P0", 0, 0, 2308)]

    for resource in P0_resource:
        name = resource.name
        price_buy = resource.price_buy
        price_sell = resource.price_sell
        pi_level = resource.pi_level
        type_id = resource.type_id
        c.execute("INSERT INTO resource VALUES ('%s','%s','%f','%f','%i')" % (name, pi_level, price_buy, price_sell, type_id))

    conn.commit()
    conn.close()

def main():
    planetary_interaction_resources()



if __name__ == "__main__":
    main()