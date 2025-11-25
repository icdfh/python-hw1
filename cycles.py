# for i in range(1, 10):
#     print(i) База циклов

# for i in range(0, 20, 2)
#     print(Это у нас чисто четные)

# for i in range( 10, 0, -2):
#     print(i)

# word = "python"

# for i in word:
#     print(i)



# text = "abaqwetasdxcahjlkaqwea"
# sum = 0
# for i in text:
#     if i == "w":
#         sum += 1
# print("Количество букв 'a'", sum)

# WHILE

# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# i = 10

# while i >= 1:
#     print(i)
#     i -= 1
# print("Старт")

# total = 0
# num = int(input("Введите число (0 => Стоп): "))

# while num != 0:
#     total += num
#     num = int(input("Введите число (0 => Стоп): "))
# print("Сумма: ", total)



# secret = 7
# attempt = int(input("Угадай число: "))

# while attempt != secret:
#     print("Неверно")
#     attempt = int(input("Угадай число: "))
# print("Молодец")


# Сумма всех чисел от 1 до 50 включительно

# Сумма всех четных от 1 до 100 включительно


# Найти количество отрицательных чисел -10 -> 5


# break/continue/pass

# 12345678910
# break
# continue


# word = "kaboom"

# for i in word:
#     if i == "a":
#         print("Найдена буква а")
#         break
# print("Смотрим", i)

# for i in range(0,10):
#     print(i)
#     if(i == 4):
#         print("Остановка!")
#         break

# while True:
#     num = int(input("Введи число (отрицательное = СТОП): "))

#     if num < 0:
#         print("Цикл остановлен")
#         break

#     print("Ты ввёл", num)

# secret = 5

# while True:
#     x = int(input("Угадай число: "))

#     if x == secret:
#         print("Угадал")
#         break
#     print("Не угадал")

# for i in range(1,21):
#     if i % 2 != 0:
#         continue
#     print("Четное", i)

# while True:
#     text = input("Введите текст ('stop' -> выход): ")

#     if text == "stop":
#         break

#     if text == "":
#         continue

#     print("Вы ввели", text)

# word = "programming"

# for i in word:
#     if i not in "aeiou":
#         continue
#     print("Гласная", i) 

# pass временно пустой блок(заглушгка)

# for i in range(5):
#     if i == 3:
#         pass
#     print(i)

# def qwerty():
#     pass


print("-------Мини касса--------")
print("Введите цену товара. 'pay' -> завершить: ")

total = 0
while True:
    data = input("Цена: ")

    if data == "pay":
        break
    
    if data == "":
        continue

    price = float(data)

    if price < 0:
        print("Цена не может быть меньше 0")
        continue

    total += price
    print("Текущая сумма: ", total)

print("Итого к оплате", total)
