sonlar_soni = int(input("kiritiladigan sonlar sonini kiriting: "))

if sonlar_soni > 1:
    num1 = int(input("1-sonni kiriting: "))

    max = num1
    min = num1

    for i in range(2, sonlar_soni+1):
        num = int(input(f"{i}-sonni kiriting: "))
        if num > max:
            max = num
        
        if num < min:
            min = num
    
    result = (min + max) / 2 
    print(result)

elif sonlar_soni == 1:
    num1 = int(input("sonni kiriting: "))
    
    print(num1)
    
else:
    print("sonlar soni musbat bo'lishligi kerak")