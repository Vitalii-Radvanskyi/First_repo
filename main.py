n =  int(input("Число: "))
if n >= 0:
    if n == 0:
        print("Нуль")
    else:
        print("Додатнє")
else:
    print("Відємне число")  
    
temp = int(input("Температура: "))
if temp >= 0:
    if temp >= 20:
        print("Тепло")
    else:
        print("Прохолодно")
else:
    print("Холодно")
    
age = int(input("Вік: "))
has_tiket = (True or False) # я незрозумів (True or False) це на вибір ?
if age >= 18:
    if has_tiket:
        print("Можна зайти")
    else:
        ("Немає квитка")
else:
    print("Замалий вік")            
    
score = int(input("Ведіть оцінку : "))
if score >= 60:
    if score >= 90:
        print("Відмінно")
    else:
        print("Зараховано")
else:
    print("Не зараховано") 
    
hours = int(input(""))
if hours < 12:
    if hours < 6:
        print("Ніч")
    else:
        print("Ранок")
else:
    if hours < 18:
        print("День")
    else:
        print("Вечір")                  
                
age = 16
my_age ="+18" age >= 18 or "Не 18"
print(my_age)
              