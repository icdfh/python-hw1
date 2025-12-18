# Это наша база
products = []
# Функция добавление товара
def add_product(name,price):
    product = {
        "name": name,
        "price": price
    }
    products.append(product)

# Функция вывода товара
def show_products():
    if len(products) == 0:
        print("Товаров нет")
        return
    index = 1
    for product in products:
        print(index, ".", product["name"], "-", product["price"], "Тенге")
        index += 1

# Функция подсчета общей суммы
def get_total_price():
    total = 0
    for product in products:
        total += product["price"]
    return total
    
# Функция меню
def show_menu():
    print("\n1. Добавить товар")
    print("2. Показать товары")
    print("3. Показать общую сумму")
    print("0. Выход")


while(True):
    show_menu()
    choice = input("Выберите действие: ")
    if choice == "1":
        name = input("Название товара: ")
        price = int(input("Цена товара: "))
        add_product(name,price)
    elif choice == "2":
        show_products()
    elif choice == "3":
        total = get_total_price()
        print("Общая сумма:", total,"Тенге")
    elif choice == "0":
        print("Выход из системы")
        break
    else:
        print("Неверный выбор")