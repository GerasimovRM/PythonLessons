# есть 3 товаров. вычислить общую цену

# total_price = 0
# count = 0
# while count < 3:
#     price = float(input())
#     total_price += price
#     count += 1
# print("Сумма введенных чисел равна", total_price)


total_price = 0
for i in range(3):
    price = float(input())
    total_price += price
print("Сумма введенных чисел равна", total_price)