#Vers.1
def comp_interest(sum):
    int_rate = 4 
    f_year = sum * (1 + int_rate / 12) ** (1 * 1)
    s_year = sum * (1 + int_rate / 12) ** (1 * 2)
    t_year = sum * (1 + int_rate / 12) ** (1 * 3)
    print("\nYou invested %.2f. \nIn a year that will be %.2f. \nIn two %.2f. \
    \nIn three that will amount to %.2f!" % (sum, f_year, s_year, t_year))
    
comp_interest(5000) 
comp_interest(2000)

#Vers.2
def comp_interest():
    sum = int(input("Please enter a sum of your deposit: "))
    int_rate = 4 
    f_year = sum * (1 + int_rate / 12) ** (1 * 1)
    s_year = sum * (1 + int_rate / 12) ** (1 * 2)
    t_year = sum * (1 + int_rate / 12) ** (1 * 3)
    print("\nYou invested %d. \nIn a year that will be %.2f. \nIn two %.2f. \
    \nIn three that will amount to %.2f!\n\n" % (sum, f_year, s_year, t_year))
    
comp_interest() 
comp_interest()