number = input()
a = int(number[0])
b = int(number[1])
c = int(number[2])
# if a > b:
#     a, b = b, a
# if b > c:
#     b, c = c, b
# if a > b:
#     a, b = b, a

# 7 3 1
a2 = min(a, b, c)
c2 = max(a, b, c)
b2 = a + b + c - a2 - c2

print((a2 + c2) / 2 == b2)