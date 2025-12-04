# list []
# tuple ()

# numbers = [10,20,30,40,50]
# mix = [10,20,True, "qwerty", 3.14]
# names = ["Diana", "Dias", "Mansur"]
#         #    0  1  2  3  4
# print(numbers[0]) 
# print(numbers[-1])
# print(numbers[-2])

# numbers = [10,20,30,40,50]
# numbers[0] = "qwerty"
# numbers.append(40)
# numbers.insert(4, 40)

# append
# insert
# len
# pop(), pop(i)
# remove удалял по элементу
# clear
# sort
# reverse
# count
# copy
# extend
# min
# max
# sum

# numbers = [10,20,30,40,50]
# numbers.pop()
# print(numbers)

# numbers = [10,20,30,40,50]
# print(numbers[:5])

# numbers = [5,41,1,7,4,50]
# numbers.sort()
# print()

# nums = []

# for i in range(5):
#     a = int(input("Введите число: "))
#     nums.append(a)

# total = 0 
# for i in nums:
#     total += i

# print(nums)
# print(total)

# Дан список оценок:
# grades = [50, 90, 75, 100, 60, 88]

# Найти максимальную оценку

# Посчитать среднюю

# Сколько оценок ≥ 80?

# grades = [50, 90, 75, 100, 60, 88]

# max_grade = grades[0]

# # Макс число
# for i in grades:
#     if i > max_grade:
#         max_grade = i

# # Среднее
# total = 0 
# for i in grades:
#     total += i
# avg = total / len(grades)


# count_good = 0
# for i in grades:
#     if i >= 80:
#         count_good += 1

# print(max_grade)
# print(avg)
# print(count_good)


# Для списка заказов
# [id, цена]: найдите сумму,
# минимальную цену и её id.

# orders = [
#     [301, 990], 
#     [302, 12000],
#     [303, 2000],
#     [304, 10000],
#     [305, 5000],
# ]

# total = 0
# for i in orders:
#     total += i[1]

# min_price = orders[0][1]
# min_id = orders[0][0]

# for i in orders:
#     order_id = i[0]
#     price = i[1]

# if price < min_price:
#     min_price = price
#     min_id = order_id

# print(total)
# print(min_price)
# print(min_id)

# --------------КОРТЕЖИ tuple----------------

# numbers = (10,20,30)
# print(numbers[-1])

# Индексы и срезы одинаковые

# t = (2,4,1,5,78,3,10)
# # t.sort()
# print(t[0])
# print(t[-1])
# print(t[1:3])
# print(t)

# a = (1) 
# t = (1,)
# print(type(a))
# print(type(t))

# lst = [1,2,3]
# t = tuple(lst)

# t2 = (10,20,30)
# lst2 = list(t2)

# print(type(t))
# print(type(lst2))


# t = (
#     [100,200,300],
#     [100,200,300],
#     [100,200,300],
#     [100,200,300],
#     [100,200,300],
# )

# ----------------------СТРОКИ------------------------------

# a = "qwerty"

# for i in a:
#     print(i)


# text = "Python"

# print(text[0])
# print(text[-1])
# print(len(text))


# text = "Python"

# print(text[0:2])
# print(text[2:5])
# print(text[:3])
# print(text[3:])
# print(text[::-1])


# методы изменения РЕГИСТРА

# name = "dIaS"

# print(name.lower())
# print(name.upper())
# print("hello world".title())
# print(name.capitalize()) исправляет текст 

# name = input("Введите имя: ")

# clean_name = name.lower().capitalize().strip()
# print("Привет", clean_name)


# raw = "       Dias      \n"

# print("[" + raw + "]")
# print("[" + raw.strip() + "]")
# lstrip()
# rstrip()

# replace замена текста

# text = "I like JS. JS is cool" 

# new_text = text.replace("JS", "Python")
# print(new_text)

# text = "hello world everthing is good "
# print(text.replace(" ", "_"))

# text = "I love Python lang prog"
# words = text.split()

# print(words)
# print(len(words))

# data = "-Dias-18-95-"
# parts = data.split("-")
# print(parts)

# words = ["I", "hate", "C++"]

# words2 = ",".join(words)
# print(words2)

# in find()

# text = "Hello World"
# print("World" in text)
# print("cat" in text)

# print(text.find("World"))
# print(text.find("cat"))
# print(text.find("l"))


# lower()
# upper()
# capitalize() -> превращает любой текст в обычный mAdIYAR -> Madiyar
# strip()  -> убирает пробелы сверху есть примеры
# lstrip() -> убирает пробелы только с левой стороны
# rstrip() -> убирает пробелы только с правой стороны
# find()
# title()
# ::-1 reverse как в массиве
# join() из массива в текст
# split из текста в массив
# replace("Указываем значение которое хотим поменять", "на то что хотим поменять")

# new = "val ue"
# print(new.strip())

# 1.Пользователь вводит своё имя.
# Выведите Привет, <Имя>!,
# где имя приведено к нормальному виду
# (первая буква заглавная, лишние пробелы убраны).

# name = input("Введите ваше имя : ")
# clean = name.strip().lower().capitalize()
# print(f"Привет, {clean}! ")



# 2.Пользователь вводит строку.
# Выведите:

# количество символов

# количество пробелов

# text = input("Введите текст: ")

# length = len(text)
# spaces = 0
# for i in text:
#     if i == " ":
#         spaces += 1

# print(length)
# print(spaces)

# .Пользователь вводит предложение.
# Выведите количество слов.

# text = input("Введите предложение: ")
# words = text.split()
# print(words)
# print("Слов: ", len(words))


# 4.Пользователь вводит строку.
# Сделайте так, чтобы:

# все буквы были маленькими

# все пробелы заменены на _

# text = input("Введите что-то:")
# text = text.lower()
# text = text.replace(" ", "_")

# print(text)


# 5.Пользователь вводит слово.
# Посчитайте, 
# сколько 
# в нём гласных букв (а, о, е, ё, и, ы, у, ю, я).


# text = input("Введте слово: ")
# vowels = "аоеёиыуюя"
# count = 0

# for i in text:
#     if i in vowels:
#         count += 1
# print(count)

# a = 5

# include <iostream>
# include <string>

# using namespace std

# int main(){
#     let a = 5 (Number)
#     cout << a

# }