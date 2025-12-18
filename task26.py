total = 0

for i in range(1, 8):
    age = int(input(f"{i} - talaba yoshi: "))
    
    if age < 21:
        total += age
    
print(total)