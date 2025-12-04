# replace("JS","Python")
# split("*")
# upper
# lower
# capitalize 
# title()
# find 
# in True False
# strip
# lstrip
# rstript
# join

# Список он хранит у нас просто значения
# Словарь он хранит информацию обьекта


# students = [
#     {id: 1,"fullname": "Dias", "age": 19},
#     {id: 2,"fullname": "Dias", "age": 19},
#     {id: 3,"fullname": "Dias", "age": 19},
# ]


student = {
   "name": "Dias",
   "age": 18
}
# student["grade"] = 90 добавление нового ключа и его значения
# student["age"] = 17 обновлени данных
# print(student["name"])
# student.pop("age") Удаление через метод pop
# print(student)
# print(student.get("age", "Нет данных"))
# get -> это у нас безопасный способ получение данных

# for i in student:
#     print(i)

# for i in student.values():
#     print(i)

# for key, value in student.items(): 
#     print(key, "-", value)
# items() -> сделать перебор по всему обьекту

# values() дает возможность сделать перебор именно значений

# crud -> 
# Create
# R - read/show
# u - update
# d - delete

# user = {
#    "name": "Dias",
#    "age": 18,
#    "scores": {
#        "math": 90,
#        "python": 100,
#        "dev":{
#            "frontend":{
#                "lang1": "Html",
#                "lang1": "css",
#                "JS":{
#                    "JS1": "React",
#                    "JS2": "Vue"
#                }
#            },
#            "backend":{
               
#            }

#        }
#    }
# }
# print(user["scores"]["dev"][])
# Сверху пример не испольузем 


# 1.
# students ={
#     "Dias": 100,
#     "Madina": 95,
#     "Aruzhan": 60,
    
# }

# for name, score in students.items():
#     print(name, ":", score)

# # 2.
# best = max(students, key=students.get)
# print(best, students[best])

# pairs = [
#     ("Aruzhan", 16),
#     ("Dias", 17)
# ]
# pairs.append(("Aruzhan", 16))
# d = dict(pairs)
# for key, age in d.items():
#     print(key, "-",age)


users = {
    1: {"name": "Dias", "role": "admin"},
    2: {"name": "Almas", "role": "user"}
}

for user_id, info in users.items():
    print(f"ID: {user_id}, Name: {info["name"]}, Role: {info["role"]}")

for i in users:
    print(i)

for i in users.values():
    print(i["name"])