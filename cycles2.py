# for i in range(5):
#     print(i)

# range(stop)
# range(start, stop)
# range(start,stop, step)

# for i in range(1,4):
#     print(i)

# for i in range (0,10,2):
#     print(i)

# for i in range(10, 0, -1):
#     print(i)

# word = "Python"
# for i in word:
#     print(i)

# break 
# continue
# pass

# Вложеннный цикл его философия 
# Это цикл внутри друого
# Внешний цикл он отвечает за строки, а внутренний за символы внутри строки


# for i in range(2):
#     for j in range(3):
#         print("i =",  i, "j=", j)


# for i in range(1,6):
#     for j in range(1,6):
#         print("i =",  i, "j=", j)

# rows = 3
# cols = 5

# for i in range(rows):
#     for j in range(cols):
#         print("*", end="")
#     print()


# rows = int(input("Введите количество строк: "))
# col = int(input("Введите количество столбцов: "))

# for i in range(rows):
#     for j in range(col):
#         print("#", end="")
#     print()

# height = int(input("Введите высоту треугольника: "))

# for i in range (1, height + 1):
#     for j in range(i):
#         print("$", end="")
#     print()


# height = int(input("Высота: "))

# for i in range(height, 0, -1):
#     for j in range(i):
#         print("*", end="")
#     print("")

# n = int(input("Введите размер квадрата: "))

# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n -1:
#             print("*", end="")
#         else:
#             if j == 0 or j == n -1:
#                 print("*", end="")
#             else:
#                 print(" ", end="")
#     print()

# 1. Количество символов в строке (через цикл)

# Пользователь вводит слово.
# Вывести, сколько символов в слове, не используя len(), а используя цикл.

# word = input("Введите ваше слово: ")

# count = 0
# for i in word:
#     count += 2
# print("Количество символов", count)

# 2. Подсчитать сумму всех чётных чисел от 1 до N

# Пользователь вводит число N.
# С помощью цикла найти сумму всех чётных чисел от 1 до N включительно.

# n = int(input("Число: "))

# sum = 0
# for i in range(1, n + 1):
#     if i % 2 == 0:
#         sum += i
# print("Сумма всех четных чиctk =", sum)


# Напечатать строку N раз

# Пользователь вводит фразу и число N.
# Вывести эту фразу на экране N раз, используя цикл.

# word = input("Слово: ")
# n = int(input("Число: "))

# for i in range(n):
#     print(word)

# Пользователь вводит число N.
# Вывести таблицу:

# 1 → 1
# 2 → 4
# 3 → 9
# 4 → 16
# ...


# То есть каждое число и его квадрат

# n = int(input("Введите число: "))

# for i in range(1, n + 1):
#     print(i, "-", i * i)


# 5. Нарисовать квадрат из символов

# Пользователь вводит число N.
# Нарисовать квадрат N x N из символа @.

# Пример для N = 4:

# @@@@
# @@@@
# @@@@
# @@@@

# n = int(input("Введите число: "))

# for i in range(n):
#     for j in range(n):
#         print("@", end="")
#     print()


# 6. Нарисовать треугольник справа

# Пользователь вводит N.
# Нарисовать правосторонний треугольник:

# Для N = 5:

#     *
#    **
#   ***
#  ****
# *****


# (нужны вложенные циклы: сначала пробелы, потом *)

# n = int(input("Введите число: "))

# for i in range(1, n + 1):
#     for space in range(n-i):
#         print(" ", end="")
#     for j in range(i):
#         print("*", end="")
#     print()



# Найти количество цифр в числе

# Пользователь вводит целое число (например: 38291).
# Нужно посчитать, сколько в нём цифр, не используя строки.

# Работа через цикл и деление:

# 38291 → 5 цифр

# n = int(input("Введите число: "))
# if(n == 0):
#     print(1)
# else:
#     count = 0
#     number = abs(n)

#     while number > 0:
#         number //= 10
#         count += 1
#     print("Количество цифр", count)


#  СЛОЖНЫЕ ЗАДАЧИ (8–10)
# 8. Нарисовать “лесенку чисел”

# Пользователь вводит N.
# Нужно вывести такую фигуру:

# Для N = 5:

# 1
# 12
# 123
# 1234
# 12345

# n = int(input("Введите число: "))
# for i in range(1, n + 1):
#     for j in range(1, 5):
#         print(j, end="")
#     print()
