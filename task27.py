soni = int(input("mahsulotlar sonini kiriting: "))

total = 0

for i in range(1 , soni+1):
    narx = float(input(f"{i} - narx: "))
    
    total += narx - narx * 0.1

print(total)