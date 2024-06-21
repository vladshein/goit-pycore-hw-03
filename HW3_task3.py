# home work 3, task 3
import re

def normalize_phone(phone_number):
    #check input
    if(not isinstance(phone_number, str)):
        print("Provided phone number is not in string format")
        return None
    
    #delete all symbols, except digits(+ sign is also deleted, in case it is found inside)
    pattern = r"[^0-9+]"
    phone_with_deleted_symbols = re.sub(pattern, "", phone_number)

    print(phone_with_deleted_symbols)

    #check the country code and take action if needed
    if(re.search(r"^\+38", phone_with_deleted_symbols)):
        print("Phone starts with country code. Action not needed")
        return phone_with_deleted_symbols
    elif(re.search(r"^38", phone_with_deleted_symbols)):
        print("Phone starts with country code without +. Add it" )
        phone_with_deleted_symbols = "+" + phone_with_deleted_symbols
        print(phone_with_deleted_symbols)
        return phone_with_deleted_symbols
    else:
        print("Phone does not start with country code. Add it")
        phone_with_deleted_symbols = "+38" + phone_with_deleted_symbols
        
        print(phone_with_deleted_symbols)
        return phone_with_deleted_symbols

#test data
phone1 = "+38-099-444-4444"
phone2 = "(099)-444-4444"
phone3 = "38099444444"
phone4 = "   (+38099)444-4444"

#call test data
normalize_phone(phone1) 
normalize_phone(phone2) 
normalize_phone(phone3) 
normalize_phone(phone4) 
