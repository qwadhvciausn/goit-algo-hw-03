# task 1
from datetime import datetime

def get_days_from_today(date):
    input_date = datetime.strptime(date, "%Y-%m-%d").date()
    date_now = datetime.today().date()
    x = (input_date - date_now).days
    return x
except ValueError:
    return "Написано y невідповідному форматі дату"
# task 2
import random

def get_numbers_ticket(min, max, quantity):
    if min >= 1 and max < 1000 and min < quantity < max:
       my_list = random.sample(range(min, max + 1), quantity)
       return sorted(my_list)      
    else:
        return []
# task 3
import re
 def normalize_phone(phone_number):
    phone_number = re.sub(r"[^\d+]", "", phone_number)
    if phone_number.startswith("38"):
        return "+" + phone_number
    elif phone_number.startswith("0"):
        return "+38" + phone_number
    else:
        return phone_number
        