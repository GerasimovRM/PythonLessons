print('Введите имена двух братьев из античных мифов и легенд.')
brother1 = input()
brother2 = input()
if (brother1 == 'Ромул' and brother2 == 'Рем' or brother1 == 'Кастор' and
        (brother2 == 'Поллукс' or brother2 == 'Полидевк')):
    print('Верно.')
else:
    print('Неверно.')
