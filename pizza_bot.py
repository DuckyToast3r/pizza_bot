# Pizza Bot program 
import random
from random import randint 

# List of random names 
names = ["Mark", "Pheobe", "sally", "Michael", "Denise", "Ellen,"]

# Welcome message with random name 

def welcome():  
    '''
    Purpose: To generate a random name from the list and print out 
    a welcome message 
    Paramerters: None 
    Returns: None  
    '''
    num = randint(0,9)
    name = (names[num])
    print("*** Welcome to Dream Pizza   ")
    print("*** My name is",name, "***")
    print("***I will be here to help you order your delicious Dream Pizza***")


# Menu for pickup delivery 






# Pick up information - name and phone number 






# Delivery informaiton - name address and phone 





# Choose number of Pizzas - max5 






# Pizza menu 






# Pizza order - from menu - print each pizza order with cast 





# Print order out - including if order is del or pick up and add names and price of each pizza - Total cost including any delivery charge 




# Ability to cancel or proceed with order 





# Option for new order or to exit 







# Main function 
def main():
    '''
    Purpose: To run all functions  
    a welcome message 
    Paramerters: None 
    Returns: None  
    '''
    welcome()

main() 
