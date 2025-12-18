# student = {
#     "name": "Qwerty",
#     "age": "19"
# }
# # Доступ
# print(student["name"])
# print(student.get("name", "Такого ключа нет"))

# изменение значения

# student["age"] = 21
# print(student)

# добавление нового ключа
# student["city"] = "Almaty"
# удаление
# remove = student.pop("age")


# чистый цикл .keys()
# .values()
# .items()

# for keys,elements in student.items()

# fruits = [
#     {},
#     {}
# ]
# fruits = {
#     [],
#     [],
#     [],
# }
# fruits = [
#     {id: 1, "scores":[50,60,70,80]}
#     {id: 2, "scores":(14,55,67,89)}
# ]

# Список -> словарь мы всегда обращаемся через индекс
# Словарь -> ключи 

# 1.
# person = {
#     "name": "Askar",
#     "age": 20,
#     "city": "Aktobe"
# }

# person["age"] = person["age"] + 5
# print(person)

# 2.
# students = [
#     {"name": "Ali", "score": 75},
#     {"name": "Ali", "score": 89},
#     {"name": "Ali", "score": 95},
# ]
# for student in students:
#     if student["score"] > 80:
#         print(student["name"])

# Вывести имена студентов у которых score > 80
# 3.
# db = {
#     "python": {"students": 23, "teacher": "Adil"},
#     "js": {"students": 17, "teacher": "Dana"}
# }
# # Вывести количество студентов по каждому направлению
# # в фромате:
# # python:23
# # js:17

# for key, info in db.items():
#     print(key + ":", info["teacher"])
# 4.
# grades = {
#     "A": [90,80,70],
#     "B": [82,71,63],
#     "C": [57,48]
# }
# for key, scores in grades.items():
#     total = sum(scores)
#     count = len(scores)
#     average = total / count
#     print(average)

# Для каждой группы посчитать средний балл

# 5. 
# orders = {
#     "A":[12,13,23,45],
# }
# for i,grades in orders.items():
#     total = sum(grades)
#     print(total)


# Найти сумму всех заказов со статусом "paid"
# total = 0

# for i in orders:
#     if i["status"] == "paid":
#         total += i["price"]
#     print(i["id"])
#     print(i["price"])
# print("Сумма оплаченных заказов:", total)

# users = [
#     {"name": "Ali", "role": "admin", "active": True},
#     {"name": "Adil", "role": "user", "active": False},
#     {"name": "Amir", "role": "user", "active": True},
# ]
# Вывести мена только активных пользователей
# с ролью user

# def hello():
#     print("Hello!")

# def person(name):
#     print("Hello", name)

# person("Ali")

# insert(index,value)

# def sum(a,b):
#     result = a + b
#     return result

# print(sum(3,4))

# def user(name,age,city):
#     print("Hello", name,age,city)

# user("Qwerty",21,"Astana")

# def square(x):
#     return x * x
    
# print(square(2))

# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
    
# print(is_even(4))
# print(is_even(7))

# def list_num(numbers):
#     total = 0
#     for num in numbers:
#         total += num
#     return total

# result = list_num((1,2,3,4,5))
# print(result)

# def format(person):
#     name = person["name"]
#     age = person["age"]
#     result = f"Имя {name}, возраст: {age}"
#     return result

# p = {"name": "Ali", "age": 21}
# text = format(p)
# print(text)

# def format(text):
#     result = text.split(" ")
#     return result

# def formatreverse(text):
#     result = text.join()
#     return result

# a = format("qwer ty")
# b = formatreverse(a)

# print(b)


def format(text):
    result = text.strip()
    return result

# print(format("qwerty"))

# def isAdult(age):
#     if age >= 18:
#         return "Allowed"
#     else:
#         return "Denied"
    
# print(isAdult(15))

def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in word:
        if ch in vowels:
            count += 1
    return count

def count_vowels2(word):
    word2 = word.lower()
    vowels = "aeiou"
    count = 0
    for i in word2:
        if i in vowels:
            count += 1
    return count

print(count_vowels2("aUeO"))
print(count_vowels("aUeO"))