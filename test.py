print("Оцените свои навыки по 5-бальной шкале")
a = input("Я люблю публичную жизнь: ")
b = input("Я не паникую во время кризиса: ")
c = input("Я умею убеждать, когда говорю: ")
d = input("В детстве я хорошо писал сочинения: ")
f = input("Я легко нахожу общий язык с окружающими: ")

try:
    z = int(a) + int(b) + int(c) + int(d) + int(f)
except ValueError:
    print("Внесите данные в числовом формате!")
else:
    if z >= 20:
        print("Вы созданы для PR")
    if z < 20 >= 14:
        print("У вас хорошие задатки для PR")
    if z < 14:
        print("Вам многому нужно научится, но судя по всему PR не для Вас")
