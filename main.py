import random
def get_numbers_ticket(min, max, quantity):
    if max > 1000:
        return []
    if min < 0:
        return []
    if min >= max:
        return[]
    if quantity > (max - min):
        return[]
    try:
        nums = range(min, max)
        return sorted(random.sample(nums, quantity))
    
    except (TypeError, ValueError):
        return []


