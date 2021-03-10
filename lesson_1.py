# Задание №1
a = 18
b = 24
print("a =", a)
print("b =", b)
name = input("Your name: ")
project = input("Name of your project: ")
department = int(input("Your department number: "))
hour = int(input("The number of hours spent on the project: "))
print(name, "department №", department, "project", project, "hours spent", hour)
#  Задание №2
seconds = int(input("Specify the number of seconds: "))
a = (seconds // 3600)
b = ((seconds % 3600) // 60)
c = ((seconds % 3600) % 60)
print(f"{a}:{b}:{c}")
# Задание №3
a = input("Number: ")
b = (a + a)
b = int(b)
c = (a + a + a)
c = int(c)
a = int(a)
print(a + b + c)
# Задание №4
i = int(input("Number: "))
r = -1
while i > 10:
    d = i % 10
    i = i // 10
    if d > r:
        r = d
print(r)
# Задание №5
revenue = int(input("indicate your revenue: "))
сosts = int(input("Indicate your costs: "))
a = revenue - сosts
b = сosts - revenue
if revenue > сosts:
    print("Profit", a)
else:
    print("Loss", b)
profitability = сosts / revenue
print("Profitability:", profitability)
employees = int(input("Indicate the number of employees: "))
c = a / employees
d = b / employees
if revenue > сosts:
    print("Profit per employee", c)
else:
    print("Loss per employee", d)
# Задание №6
a = 2
b = 3
c = 0
while True:
    a = a + a * 0.1
    c = c + 1
    print(c, "-й день:", a)
    if a > b:
        break
