from datetime import datetime, timedelta, date
# today = datetime.now()
# future = today + timedelta(days=10)

# print(future)


# date_str = "2026.03.15"
# date_objc = datetime.strptime(date_str, "%Y.%m.%d").date()
# future = date_objc + timedelta(days=30)
# future = date_objc.strftime("%Y.%m.%d")
# print(future)
# print(type(future))


# d1 = date(2026, 2, 1)
# d2 = date(2026, 2, 20)
# if d1 < d2:
#     print("d1 earlier")
# elif d1 == d2:
#     print("Same date")
# else:
#     print("d1 later")       


# d = date(2026, 2, 7)  #Кейс перший якщо хоч знати який точно день сихідних(В разі чого я для себе)
# d = d.weekday()
# if d == 5:
#     print("Suturday")
# elif d == 6:
#     print("Sunday")
# else:
#     print("Workday")
    
    
d = date(2026, 2, 7) # Кейс два якщо простот вихідні і будні  (В разі чого я для себе)
d = d.weekday()
if d >= 5:
    print("Weekend")  
else:
    print("Workday")  
    
birthday = (1995, 2, 5)

