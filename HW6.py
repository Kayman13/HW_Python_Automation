
# pylint: disable=invalid-name

# Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'

http = "www.my_site.com#about"
print(http.replace("#", "/"))

# Напишите программу, которая добавляет ‘ing’ к словам

text = "train"
print(text + "ing")

# В строке "Ivanou Ivan" поменяйте местами слова => "Ivan Ivanou"

name = "Ivanou Ivan"
splitStr = name.split()
print(splitStr[1] + " " + splitStr[0])

# Напишите программу, которая удаляет пробел в начале, в конце строки

delSpaceFirst = "word First "
print(delSpaceFirst.rstrip("r"))
delSpaceSecond = "  second Word"
print(delSpaceSecond.lstrip())
delSpaceThree = " Three Words "
print(delSpaceThree.strip())

# Имена собственные всегда начинаются с заглавной буквы, за которой следуют строчные буквы.
# Исправьте данное имя собственное так,
# чтобы оно соответствовало этому утверждению. "pARiS" >> "Paris"

txt = 'pARiS'
print(txt.capitalize())

# Перевести строку в список "Robin Singh" => ["Robin", "Singh"],
# "I love arrays they are my favorite" =>
# ["I", "love", "arrays", "they", "are", "my", "favorite"]

messageStr = "Robin Singh"
arr = messageStr.split()
print(arr)
messageStrSecond = "I love arrays they are my favorite"
arrSecond = messageStrSecond.split()
print(arrSecond)

# Дан список: [Robin Singh], и 2 строки: "Welcome" и "airport".
# Напечатайте текст: “Hello, Robin Singh! Welcome to airport”

text1 = ["Robin Singh"]
str1 = "Welcome"
str2 = "airport"
print(f"Hello, {text1[0]}! {str1} to {str2}")

# Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"]
# сделайте из него строку => "I love arrays they are my favorite"

msg = ["I", "love", "arrays", "they", "are", "my", "favorite"]
results = " ".join(msg)
print(results)

# Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,
# удалите элемент из списка под индексом 6

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.insert(2, 13)
del numbers[6]
print(numbers)
