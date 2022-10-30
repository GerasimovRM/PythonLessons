print("Как у тебя дела?")
text = input()
if text == "заебись" or text == "отлично":
    print("Это заебись!")
    print("А чому так???")
    text2 = input()
    print("Рад за тебя!")
elif text == "хуево" or text == "плохо" or text == "не очень":
    print("Да не серчай, все гуд будет!")
else:
    print("Я тебя не понял, но надеюсь у тебя все хорошо!")
