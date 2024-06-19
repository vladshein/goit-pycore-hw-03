#home work #3, task 2
import random

#function to generate list of unique random numbers in requested range  
def get_numbers_ticket(min, max, quantity):
    print("=========================")
    print("get_numbers_ticket start")
    
    #create an empty list for further fulfillment
    quantity_list = []

    #check input parameters and return empty list in case of issues
    if min < 1:
        print("Min number is less then 1")
        return quantity_list 
    if max > 1000 or max < min:
        print("Max number is incorrect")
        return quantity_list
    if (quantity > max) or (quantity < min):
        print("Quantity number is incorrect")
        return quantity_list
    
    #append the list with unique random numbers 
    while(len(quantity_list) != quantity):
        #generate random number in range min-max
        random_number = random.randint(min, max)
        
        #check if generated random number is already in the list
        if random_number in quantity_list:
            continue
        
        #add generated unique number to a list
        quantity_list.append(random_number)
    
    #sort received list and 
    quantity_list.sort()
    return quantity_list

#test data 1 
list1 = get_numbers_ticket(1, 10, 3)
print(list1)

#test data 2
list2 = get_numbers_ticket(10, 100, 17)
print(list2)

#test data 3
list3 = get_numbers_ticket(-1, 10, 3)
print(list3)


