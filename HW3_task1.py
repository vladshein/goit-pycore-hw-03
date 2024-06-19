#home work #3, task 1
from datetime import datetime
from datetime import timedelta
import re

#count days difference between current and requested day
def get_days_from_now(date):
    print("=======================")
    print("Get days from now start")
    
    #check received date string
    #if provided parameter is not string return None
    check_str = isinstance(date, str)
    if check_str:
        print("Provided date is string")
    else:
        print("Provided date parameter is not a string")
        return None
    print(date)

    #check the format of provided date string 
    date_format = r"^\d{4}-\d{2}-\d{2}$"
    date_match = re.search(date_format, date)

    #if parameter date has correct format, print it    
    if date_match:
        print(date_match)
    #if format is incorrect, return None
    else:
        print("Date format is incorrect")
        return None

    #convert string to a datetime object
    parsed_date = datetime.strptime(date, "%Y-%m-%d")

    #receive current time
    current_date = datetime.now()

    #check the diff between dates
    diff = parsed_date - current_date
    print(diff.days)
    print("Get days from now finish")
    print("=======================")
    return diff.days

#test data
date = "2022-10-22"
date2 = "2022-aaa-222"
date3 = 1111

#call get_days_from_now with test data
count = get_days_from_now(date)
print(count)
count = get_days_from_now(date2)
print(count)
count = get_days_from_now(date3)
print(count)