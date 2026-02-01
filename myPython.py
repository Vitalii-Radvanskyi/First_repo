from datetime import datetime
def get_days_from_today(date_str):
    try:
        date_objc = datetime.strptime(date_str, "%Y.%m.%d")
        time_today = datetime.today()
        deff_time = time_today - date_objc
        return deff_time.days
    except ValueError:
        return None


import random
def get_number_ticket(min, max, quantity):
    try:
        nums = range(min, max) 
        return random.sample(nums, quantity)
    except (TypeError, ValueError):
        return None
