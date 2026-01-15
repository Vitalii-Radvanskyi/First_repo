data = 'info'
if data == 'info':
    correct = True
else:
    correct = False
print(correct)   
data = 'info'
correct = True if data == 'info' else False
print(correct)
print("\n\n\n")

for i in range(0, 100, 10):
         print(i)
print("\n\n\n")
word = 'Наташа'   
for i in word:
    if i == 'т':
        print('Літера Т є в цьому слові')
        break
    else:
        print("в цьому слові немає літери Т")
              
for i in range(1, 11):
    if i % 2 == 0:
        continue
    if i == 7:
        break
    print("el:", i )
        