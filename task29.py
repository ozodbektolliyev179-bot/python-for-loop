soni = int(input("savdo nuqtalari soni: "))

total = 0

if soni > 0:
    for i in range(1 , soni+1):
        narx = int(input(f"{i} - markaz narxi: "))
        
        total += narx
    
print(total/soni)