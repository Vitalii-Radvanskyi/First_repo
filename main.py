price_burger = 5.49
price_cola = 1.99
num_burger = int(input("Кількість Бургерів:"))
num_cola = int(input("Кількість Коли:"))
cost_no_GST = num_burger * price_burger + num_cola * price_cola
GST = float((cost_no_GST) * 0.05)
total_cost = cost_no_GST + GST
full_dolars = int(total_cost)
total_cents = int(total_cost * 100)
print("Повних доларів:", full_dolars)
print("Загальна вартість у центах:", total_cents)
