num1 = int(input("1-son: "))
num2 = int(input("2-son: "))

if num1 <= num2:
    for i in range(num1, num2+1):
        print(i)
else:
    for i in range(num1, num2-1, -1):
        print(i)