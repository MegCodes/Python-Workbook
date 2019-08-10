#Vers.1
print("Somebody Someone")
print("City of Love")
print("Lalaland")

#Vers.2
def mailing_address():
    name = input("Please enter your name: ")
    address = input("Please enter your address: ")
    country = input("Please enter your country: ")

    print("\nName: %s \nAddress: %s \nCountry: %s" % (name,address,country))

mailing_address()

#Vers.3
def mailing_address(name, address, country):
    print ("\nName: %s \nAddress: %s \nCountry: %s" % (name, address, country))

mailing_address("Pusya", "Bubblestreet", "Queensrose")

#Vers.4
def mailing_address():
    name = input("Please enter your name: ")
    address = input("Please enter your address: ")
    country = input("Please enter your country: ")

    print("\nName: {} \nAddress: {} \nCountry: {}".format(name,address,country))

mailing_address()

#Vers.5
def mailing_address(name, address, country):
    print ("\nName: {} \nAddress: {} \nCountry: {}".format(name,address,country))

mailing_address("Pusya", "Bubblestreet", "Queensrose")

#Vers.6
def mailing_address():
    name = input("Please enter your name: ")
    address = input("Please enter your address: ")
    country = input("Please enter your country: ")

    print(f"\nName: {name} \nAddress: {address} \nCountry: {country}")

mailing_address()

#Vers.7
def mailing_address(name, address, country):
    print (f"\nName: {name} \nAddress: {address} \nCountry: {country}")

mailing_address("Pusya", "Bubblestreet", "Queensrose")

#Vers.8
class Address():

    def __init__(self,name,address,country):
        self.name = name.title()
        self.address = address.title()
        self.country = country.title()

    def show_me_where(self):
        print("\nName: %s \nAddress: %s \nCountry: %s" % (self.name, self.address, self.country))


claire = Address("claire", "city of love", "ukraine")
donna = Address('donna', 'big cool city', 'dreamland')
cristiano = Address ('cristiano ronaldo', 'madeira', 'portugal')

claire.show_me_where()
donna.show_me_where()
cristiano.show_me_where()