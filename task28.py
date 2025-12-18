ball = int(input("1-talaba bali: "))

max = ball
min = ball

for i in range(2 , 6):
    ball = int(input(f"{i} - talaba bali: "))
    if ball > max:
        max = ball
    if ball < min:
        min = ball
    
print(f"Eng yuqori: {max}, Eng past: {min}")