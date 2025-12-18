

telefonlar_soni = int(input("kiritiladigan telefonlar sonini kiriting: "))

sum = 0

if telefonlar_soni >= 1:
    for i in range(1 , telefonlar_soni + 1):
        narxi = float(input(f"{i}-narx: "))
        if narxi % 5 == 0:
            sum += narxi
    
    print(sum)
else:
    print("sonlar soni musbat bo'lishligi kerak")
