#Vers.1
def greeting():
    name = input("Please enter your name: ").title()
    print("Hello and welcome " + name + "!")

greeting()

#Vers.2
def greeting():
    name = input("Please enter your name: ").title()
    print("Hello and welcome %s!" % (name))

greeting()

#Vers.3
def greeting():
    name = input("Please enter your name: ").title()
    print("Hello and welcome {}!".format(name))

greeting()

#Vers.4
def greeting():
    name = input("Please enter your name: ")
    print(f"Hello and welcome {name}!")

greeting()

#Functions with given values
#Vers.5
def greeting(name):
    print(f"Hello and welcome {name.title()}!")

greeting('donna')

#Vers.6
def greeting(name):
    print("Hello and welcome {}!".format(name.title()))

greeting('donna')

#Vers.7
def greeting(name):
    print("Hello and welcome %s!" % (name.title()))

greeting('donna')

#Vers.8
def greeting(name):
    print("Hello and welcome " + name.title() + "!")

greeting('donna')

#Simple versions
#Vers.9
name = input("Please enter your name: ").title()
print("Hello and welcome %s!" %(name))

#Vers.10
name = input("Please enter your name: ").title()
print("Hello and welcome {}!".format(name))

#Vers.11
name = input("Please enter your name: ").title()
print("Hello and welcome " + name + "!")

#Vers.12
name = input("Please enter your name: ").title()
print(f"Hello and welcome {name}!")

#Classy version
#Vers.13
class User():
    def __init__(self, name):
        self.name = name.title()
        
    def greeting(self):
        print("Hello and welcome %s !" %(self.name))
        
donna = User('donna')
donna.greeting()

#Vers.14
class User():
    def __init__(self, name):
        self.name = name.title()
        
    def greeting(self):
        print("Hello and welcome " + self.name + "!")
        
donna = User('donna')
donna.greeting()

#Vers.15
class User():
    def __init__(self, name):
        self.name = name.title()
        
    def greeting(self):
        print("Hello and welcome {}!".format(self.name))
        
donna = User('donna')
donna.greeting()

#Vers.16
class User():
    def __init__(self, name):
        self.name = name.title()
        
    def greeting(self):
        print(f"Hello and welcome {self.name}!")
        
donna = User('donna')
donna.greeting()