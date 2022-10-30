n = int(input())
s = 0
while n != 0:
    s += n  # s = s + n => (s *= n) == (s = s * n)
    n = int(input())
print(s)
