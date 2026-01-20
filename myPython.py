nums = [5, 10, 15, 20, 25, 30]
for i in range(len(nums)-1, -1, -1):
    if nums[i] % 5 != 0 or nums[i] % 10 != 0:
        nums.remove(nums[i])
print(nums)    

letters = ['a', 'b', 'c', 'd', 'e']
for i in range(len(letters)):
    if i % 2 != 0:
        letters[i] = 'X'
print(letters) # Невдалось розвязати задачу ще повернусь 
  
nums = [1, 2, 3, 2, 4, 2, 5]
for i in range(len(nums)-1, -1, -1):
    if nums [i] != 2:
        nums.remove(nums[i])
print(len(nums))

nums = [4, 7, 10, 13, 16, 19, 22]
for i in range(len(nums)-1, -1, -1):
    if i % 2 != 0:
        nums.remove(nums[i])
print(nums)       

letters = ['p', 'y', 't', 'h', 'o', 'n']
for i in range(len(letters)):
    if i % 2 != 0:
        letters[i] = '*'
print(letters)

my_dict = {"name": "Аліна", "age": 24, "city": "Калгарі"}
my_dict["age"] = 26  # Змінює вік на 26
my_dict["email"] = "alice@example.com"  # Додає нову пару ключ-значення
del my_dict["city"]
print("name" in my_dict)

car = {
    "brand": "Toyota",
    "year": 2020
}
color = car.get("color", "Unknown") 
print(color)

person = {
    "name": "John",
    "age": 40,
    "job": "Engineer"
}
for key, value in person.items():
    print(key, "-", value)
    
scores = {
    "math": 80,
    "english": 65,
    "physics": 90
}
for key, value in scores.items():
    if value >=70:
        print(key, value)    # результвт є, але невпевнений чи код виглядає коректно

orders = [
    {"id": 1, "paid": True},
    {"id": 2, "paid": False},
    {"id": 3, "paid": True}
]
for order in orders:
    if order["paid"]:
        print(order["id"])
