# a = [1,"qwe", True]
# b = a * 3

# print(b)

# zero = [0, 2] * 5
# print(zero)

# Дан список целых чисел, Разложить их в три списка 
# отрицательные
# положительные
# нейтральные

# nums = [10, -9, -8, 0, 0, 23, -56, 11, 0, -1000, 228]

# negatives = []
# positives = []
# neutral = []

# for i in nums:
#     if i < 0:
#         negatives.append(i)
#     elif i == 0:
#         neutral.append(i)
#     else:
#         positives.append(i)
# print("Отрицательные: ", negatives)
# print("Нейтральные", neutral)
# print("Положительные", positives)

# Дан список чисел. 
# Нужно удалить из него все отрицательные элементы,
# изменяя сам список

# nums = [5, -3, 10, -7, 0, -1, 4]

# i = 0 
# while i < len(nums):
#     if nums[i] < 0:
#         nums.pop(i)
#     else:
#         i += 1
# print(nums)


# Условие 
# Все нули должныть "уплыть" в конец,
# порядок остальных чисел должен сохраниться

# nums = [0, 5, 0,3,7,0,1,2,0,9]
# result = []

# zero_count = nums.count(0)

# for i in nums:
#     if i != 0:
#         result.append(i)

# for j in range(zero_count):
#     result.append(0)
# print(result)


# Дома доработать
# nums = [0, 5, 0,3,7,0,1,2,0,9]

# for i in nums:
#     if nums[i] == 0:
#         nums.pop(i)
#         nums.append(0)
    
# print(nums)


# Есть список чисел, 
# где нужно найти 3 самых больших балла, 
# не меняя исходный список

# nums = [70, 55, 40, 60, 80, 90 ,50, 100]
# nums_copy = nums.copy()

# nums_copy.sort(reverse=True)

# top3 = nums_copy[:3]

# print("Исходный массив", nums)
# print("Топ-3", top3)


# Удалить все минимальные элементы
# nums = [3,1,5,1,7,8,20,1,2,6,7]

# Если минимальное значение встречается
# в массиве несколько раз, 
# нужно удалиь все такие элементы

# nums = [3,1,5,1,7,8,20,1,2,6,7]

# min_val = min(nums)

# while min_val in nums:
#     nums.remove(min_val)
# print(nums)

for i in range(3):
    print(i)