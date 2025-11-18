# temp = int(input("Введите температуру воздуха (целое число)"))

# if(temp <= 0):
#     print("Мороз")
# elif(temp <= 15):
#     print("Прохладно")
# elif(temp <= 30):
#     print("Жарко")
# else:
#     print("Ошибка")



# grade = int(input("Введите вашу оценку: "))
# if(grade <= 50):
#     print("Пересдача")
# elif(grade <= 70):
#     print("Все норм")
# elif(grade <= 90):
#     print("Все отлично, 40к в кармане")
# elif(grade <= 100):
#     print("А ты крут")
# else:
#     print("Вы обманываете...")

# age = int(input("Возраст: "))
# passport = input("Есть паспор? (да/нет): ")

# if(age >= 18 and passport == "да"):
#     print("Можно пойти")
# elif(age >= 18 and passport == "Да"):
#     print("Можно пойти")
# else:
#     print("Нельзя пройти")

# day = input("Введите день недели (например: Понедельник/Вторник/Cуббота): ")

# if(day == "Суббота" or day == "Воскресенье"):
#     print("Ура выходной")
# else:
#     print("Будний день...")

# age = int(input("Возраст: "))
# is_student = input("Вы студент? Да/Нет")

# if(age >= 18 or is_student == "Да"):
#     print("Можно пойти")
# else:
#     print("Нельзя пройти")

# rain = input("Идет дождь? (Да/Нет): ")
# if not rain == "да":
#     print("Можно гулять")
# else:
#     print("Берем зонт")


# Ввести имя и возраст: если возраст ≥ 18 — вывести 
# "{имя}, ты взрослый!", иначе "{имя}, ты несовершеннолетний."

# Ввести день недели: суббота/воскресенье → 
# «Выходной», иначе «Будний».

# Ввести температуру: <0 → «Мороз», 0–15 → 
# «Прохладно», 16–25 → «Тепло», >25 → «Жарко».

# Ввести цвет светофора: если цвет не «зелёный» → 
# «Стоять!», иначе «Идём!».

# Ввести «идёт дождь?» (да/нет): если не идёт →
# «Гуляем», иначе «Зонт».

# age = int(input("Возраст: "))
# has_ticket = input("Есть билет? (да/нет): ")
# is_vip = input("Вы VIP? (да/нет): ")

# if(age >= 18 and has_ticket == "да") or is_vip == "да":
#     print("Проход разрешен")
# else:
#     print("Проход запрещен")

# rain = input("Дождь да/нет: ")
# wind = input("Сильный ветер да/нет: ")
# temp = int(input("Температура: "))

# if(temp >= 20 and not rain == "да") or (temp >= 15 and not wind == "да"):
#     print("Погода подходит для прогулки")
# else:
#     print("Лучше остаться дома")

# role = input("Роль (admin/user/guest): ")
# has_key = input("Есть ключ доступа ? (да/нет): ")
# banned = input("Заблокирован? (да/нет): ")

# if(role == "admin" or (role=="user" and has_key == "да")) and not banned =="да":
#     print("Доступ разрешен")
# else:
#     print("Доступ запрешен")

# exam1 = int(input("Балл за экзамен 1: "))
# exam2 = int(input("Балл за экзамен 2: "))
# cheated = input("Было списывание да/нет: ")

# if(exam1 >= 70 and exam2 >= 70 and cheated == "нет"):
#     print("Экзамен сдан")
# else:
#     print("Экзамен не сдан или нарушение правил")

# has_coupon = input("Есть купон? (да/нет): ")
# has_promo = input("Есть промокод? (да/нет): ")
# is_vip = input("VIP клиент? (да/нет): ")

# if is_vip == "да" or (has_coupon == "да" and has_promo == "да"):
#     print("Скидка активейтед")
# else:
#     print("Скидки нет")