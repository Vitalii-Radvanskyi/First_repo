from datetime import datetime
def get_days_from_today(date_str):
    try:
        date_objc = datetime.strptime(date_str, "%Y-%m-%d")
        time_today = datetime.today()
        deff_time = time_today - date_objc
        return deff_time.days
    except ValueError:
        return None


import random
def get_number_ticket(min, max, quantity):
    if min < 0:
        return []
    if min >= max:
        return[]
    if quantity > (max - min):
        return[]
    try:
        nums = range(min, max) 
        return random.sample(nums, quantity)
    except (TypeError, ValueError):
        return []
    
    
import re
def phone_number(numbers):
    result =[]
    for digits in numbers:
        digits = re.sub(r"\D", "", digits)
        if digits.startswith("380"):
            result.append("+" + digits)
        elif digits.startswith("0"):
            result.append("+38" + digits)
        else:
            result.append("+" + digits)
    return result        
        
