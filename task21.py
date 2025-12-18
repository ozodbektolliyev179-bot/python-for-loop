n = int(input("N: "))

sum_toq = 0
sum_juft = 0

for i in range(1 , n+1):
    if i % 2 == 0:
        sum_juft += 1
    else:
        sum_toq += 1
        
print(f"Juft: {sum_juft}, Toq: {sum_toq}")
    