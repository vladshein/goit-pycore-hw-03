#home work 3, task 4
from datetime import datetime, timedelta

def get_upcoming_birthdays(users):

    congratulation_list = []
    #get current date
    current_date = datetime.now().date()
    print(f"Today is {current_date}")

    #convert birthdays to datetime objects
    for dict in users:
        for key, val in dict.items():
            dict[key] = datetime.strptime(val,"%Y.%m.%d").date()
            print(f"Converted datetime is {dict[key]}")
    print(users[0])   

    for user in users:
        for key, value in user.items():
            birthday_this_year = value.replace(year=2024)
            if birthday_this_year < current_date:
                print("Birtday will be in next year")
                continue
            else:
                delta = (birthday_this_year - current_date).days 
                print(delta)

                if delta <= 7:
                    print("Birthday is within 7 days.")
                    #check weekend case
                    congratulation_date = birthday_this_year
                    if birthday_this_year.weekday() == 5:
                        print("Birthday is on a weekend. Congratulate on Monday")
                        updated_date = int(birthday_this_year.day) + 2
                        congratulation_date = birthday_this_year.replace(day=updated_date) 
                        print(congratulation_date)
                   
                    elif birthday_this_year.weekday() == 6:
                        print("Birthday is on a weekend. Congratulate on Monday")
                        updated_date = int(birthday_this_year.day) + 1
                        congratulation_date = birthday_this_year.replace(day=updated_date) 
                        print(congratulation_date) 
                    #add name and congratulation data to list of dicts
                    local_dict = {}
                    local_dict[key] = congratulation_date
                    congratulation_list.append(local_dict)

    print(congratulation_list)
    return congratulation_list            

#test data                   
users = [{"Alex":"2022.1.10"},{"Bill":"2024.11.11"}, {"Cidny":"2000.06.23"}, {"Dock":"1999.06.22"},
         {"Elon":"1989.6.26"}]
#users.append({3:datetime.now().date()})
cograts_dates = get_upcoming_birthdays(users)
print(cograts_dates)
