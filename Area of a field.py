#draft, that is actually for convertation to acres
def fieldarea():
    length = int(float(input("Please enter the length in feet: ")))
    width = int(float(input("Please enter the width in feet: ")))
    acre_length = length / 43.560
    acre_width = width / 43.560
    print("The field's length is {}  and width is {} acres.".format(acre_length, acre_width))
    
fieldarea()    

#Vers.1
def fieldarea():
    acre = 43.560
    length = float(input("Please enter the length in feet: "))
    width = float(input("Please enter the width in feet: "))
    area = length * width / acre   
    print("The field's area is {} acres.".format(area))
    
fieldarea()

#Vers.2
def fieldarea():
    acre = 43.560
    length = float(input("Please enter the length in feet: "))
    width = float(input("Please enter the width in feet: "))
    area = round(length * width / acre, 2)   
    print("The field's area is {} acres.".format(area))
    
fieldarea()    

#Vers.3
def fieldarea(length, width):
    acre = 43.560
    area = round(length * width / acre, 2)   
    print("The field's area is {} acres.".format(area))
    
fieldarea(136.8, 123.2)    

#Vers.4
def fieldarea(length, width):
    acre = 43.560
    area = round(length * width / acre)   
    print("The field's area is {} acres.".format(area))
    
fieldarea(136.8, 123.2)   

#Vers.5
def fieldarea(length, width):
    acre = 43.560
    area = length * width / acre  
    print("The field's area is {} acres.".format(area))
    
fieldarea(136.8, 123.2)    