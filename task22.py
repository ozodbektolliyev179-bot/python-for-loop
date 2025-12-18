num = int(input("1-telefon narxi: "))

min = num
max = num

for i in range(2 , 6):
    num = int(input(f"{i}-telefon narxi: "))
    if num > max:
        max = num
    
    if num < min:
        min = num
        
result = (min + max) / 2

print(result)
 