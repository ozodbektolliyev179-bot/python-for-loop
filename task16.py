num1 = int(input("1-sonni kiriting: "))

min = num1

for i in range(2, 8):
    num = int(input(f"{i}-sonni kiriting: "))
    if num < min:
        min = num
        
print(min)