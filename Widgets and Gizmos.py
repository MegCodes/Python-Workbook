#Vers.1
def weight_calculator(w,g):
    w_weight = 75
    g_weight = 112
    total = (w * w_weight) + (g * g_weight)
    print("\nTotal order weight is ", total)
    
weight_calculator(3,4)    
weight_calculator(1,2)   
weight_calculator(1,1)   

#Vers.2
def weight_calculator(w,g):
    w_weight = 75
    g_weight = 112
    total = (w * w_weight) + (g * g_weight)
    print("\nTotal order weight is %d." % total)
    
weight_calculator(3,4)    
weight_calculator(1,2)   
weight_calculator(1,1)   

#Vers.3
def weight_calculator():
    w = int(input("Please enter the amount of widgets: "))
    g = int(input("Please enter the amount of gizmos: "))
    w_weight = 75
    g_weight = 112
    total = (w * w_weight) + (g * g_weight)
    print("\nTotal order weight is %d." % total)
    
weight_calculator()  

#Vers.4
def weight_calculator():
    w = int(input("Please enter the amount of widgets: "))
    g = int(input("Please enter the amount of gizmos: "))
    w_weight = w *75
    g_weight = g * 112
    total = w_weight + g_weight
    print("\nWidgets weight is %d.\nGizmos weight is %d.\nTotal order weights is %d." %(w_weight, \
    g_weight,total))
    
weight_calculator()    
#Vers.5

def weight_calculator():
    w = int(input("Please enter the amount of widgets: "))
    g = int(input("Please enter the amount of gizmos: "))
    w_weight = w *75
    g_weight = g * 112
    total = w_weight + g_weight
    print("\nWidgets weight is ", w_weight)
    print("\nGIzmos weight is ", g_weight)
    print("\nTotal weight is ", total)
    
weight_calculator()   

#Vers.5
def weight_calculator(w,g):
    w_weight = w *75
    g_weight = g * 112
    total = w_weight + g_weight
    print("\nWidgets weight is ", w_weight)
    print("GIzmos weight is ", g_weight)
    print("Total weight is ", total)
    
weight_calculator(3,4)    
weight_calculator(1,2)   
weight_calculator(1,1) 

#Vers.6
def weight_calculator():
    w = int(input("Please enter the amount of widgets: "))
    g = int(input("Please enter the amount of gizmos: "))
    w_weight = w *75
    g_weight = g * 112
    total = w_weight + g_weight
    print("\nWidgets weight is %d.\n\nGizmos weight is %d.\n\nTotal order weights is %d." %(w_weight, \
    g_weight,total))
    
weight_calculator() 

#Vers.7
def weight_calculator(w,g):
    w_weight = w *75
    g_weight = g * 112
    total = w_weight + g_weight
    print("\n\nWidgets weight is %d.\nGizmos weight is %d.\nTotal order weights is %d." \
    % (w_weight, g_weight, total))
    
weight_calculator(3,4)    
weight_calculator(1,2)   
weight_calculator(1,1)