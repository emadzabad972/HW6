# start
sum_temp: int = 0
for _ in range(5):
    temp: int = int(input('whats the temperature? '))
    sum_temp += temp
    while not -50 <= temp <= 45:
        print("not in range!")
        temp = int(input('whats the temperature? '))
    else:
        print("great!")
avg: float = sum_temp / 5
print(f"the average temperature is {avg}!")
