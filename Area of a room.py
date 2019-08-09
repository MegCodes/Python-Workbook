#Vers.1
def a_of_room():
    w = float(input("Please enter dot separated width of the room: "))
    l = float(input("Please enter dot separated length of the room: "))
    a = w * l
    print("Area of this room is %d meters." %(a))
    
a_of_room() 

#Vers.2
def a_of_room(w,l):
    a = w * l
    print("Area of this room is %d meters." %(a))
    
a_of_room(5.4, 3.2) 

#Vers.3
def a_of_room(w,l):
    a = w * l
    print(f"Area of this room is {a} meters.")
    
a_of_room(5.4, 3.2)

#Vers.4
def a_of_room(w,l):
    a = w * l
    print("Area of this room is {} meters.".format(a))
    
a_of_room(5.4, 3.2)

#Vers.5
def a_of_room():
    w = float(input("Please enter dot separated width of the room: "))
    l = float(input("Please enter dot separated length of the room: "))
    a = w * l
    print(f"Area of this room is {a} meters.")
    
a_of_room() 

#Vers.6
def a_of_room():
    w = float(input("Please enter dot separated width of the room: "))
    l = float(input("Please enter dot separated length of the room: "))
    a = w * l
    print("Area of this room is {} meters.".format(a))
    
a_of_room() 