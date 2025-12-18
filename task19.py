sonlar_soni = int(input("kiritiladigan sonlar sonini kiriting: "))
num1 = int(input("1-sonni kiriting: "))

if sonlar_soni > 1:
    
    max = num1

    for i in range(2, sonlar_soni+1):
        num = int(input(f"{i}-sonni kiriting: "))
        if num > max:
            max = num
        
    print(max)

else:
    print(num1)