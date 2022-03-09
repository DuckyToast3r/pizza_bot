# menu so that user can choose either pickup or delivery 

print ("Is your order for pickup or delivery?")

print (" For Delivery please enter d ")
print (" For Pickup please enter p")

delivery = int(input())

if delivery == "1":
    print ("Pickup")

elif delivery == "p": 
    print ("Delivery")    

else:
    print ("That was not a valid input")