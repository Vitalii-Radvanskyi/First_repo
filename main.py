def get_city(user):
    for key in user:
        if "city" in user:
            return "City is there"
        else:
            return "unknown"
        

user = {"name": "Vitalii", "age": 26, "city": "Calgary"}
print(get_city(user=user))


def count_word(text):
    readi_dict = {}
    