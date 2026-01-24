#1
age = 17
if age >= 18:
    print("Дорослий")
else:
    print("Неповнолітній")    
#2    
score = 72
if score >= 90:
    print("Відмінно")
elif score>= 60:
    print("Зараховано")
else:
    print("Не зараховано")
#3
age = 20
has_id = True
if age >=18 and has_id:
    print("Доступ дозволено")
else:
    print("Доступ заборонено")
#4    
is_admin = False
is_moderator = True
if is_admin or is_moderator:
    print("Права доступу є")
else:
    print("Немає прав")
#5   
is_blocked = False
if not is_blocked:
    print("Користувач активний")
else:
    print("Користувач заблокований")  
#6    
is_logged_in = True
is_blocked = False
if not is_blocked and is_logged_in:
    print("Показати dashboard")
else:
    print("Доступ заборонено") 
#7    
age = 17
has_parent_permission = True
if age >= 18 or (age >= 16 and has_parent_permission):
    print("Можна зайти")
else:                                    
    print("Не можна зайти")
##8
temp = int(input("Ведіть температуру: "))  
if temp >= 30 :
    print("Жарко")
elif temp >= 15:
    print("Норм")
else:
    print("Холодно")    
##9
login = input("Login: ")
password = input("Password: ")
is_blocked = False
if login == "admin" and password == "1234" and (not is_blocked):
    print("Welcom")
else:
    print("Access denied")        
        
 