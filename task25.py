total_age = 0

for i in range(1, 6):
    age = int(input(f"{i} - yosh: "))
    total_age += age
    
print(total_age / 5)