n = int(input())
count = 0
while n % 2 == 0 and n != 0:
    count += 1
    n //= 2
if n == 1:
    print(count)
else:
    print("НЕТ")
