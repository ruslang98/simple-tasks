# 1.Создать лист из 6 любых чисел. Отсортировать его по возрастанию
some_list = [5, 7, 2, 1, 7, 0]
some_list.sort()
print(some_list)
# 2.Создать словарь из 5 пар: int -> str, например {6: '6'}, вывести его в консоль попарно
some_dict = {5: '5', 3: '3', 8: '8', 4: '4', 1: '1'}
for key, item in some_dict.items():
    print(key, item)
# 3.Создать tuple из 10 любых дробных чисел, найти максимальное и минимальное значение в нем
some_tuple = (5, 2, 1, 7, 89, 45, 23, 46, 134, 867)
print(max(some_tuple), min(some_tuple))
# 4.Создать лист из 3 слов: ['Earth', 'Russia', 'Moscow'], соеденить все слова в единую строку,
# чтобы получилось: 'Earth -> Russia -> Moscow'
words = ['Earth', 'Russia', 'Moscow']
some_str = words[0] + ' -> ' + words[1] + ' -> ' + words[2]
print(some_str)
# 5.Взять строку '/bin:/usr/bin:/usr/local/bin' и разбить ее в список по символу ':'
way = '/bin:/usr/bin:/usr/local/bin'
print(way.split(':'))
# 6.Пройти по всем числам от 1 до 100, написать в консоль, какие из них делятся на 7, а какие - нет
for number in range(1, 100):
    print(True if number % 7 == 0 else False)
# 7.Создать матрицу любых чисел 3 на 4, сначала вывести все строки, потом все столбцы
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]
for row in matrix:
    print(row)
for row in matrix:
    for column in row:
        print(column)
# 8.Создать список любых объектов, в цикле напечатать в консоль: объект и его индекс
objects = ['Moscow', 'Czech', 'Europe', 48]
for i in enumerate(objects, start=1):
    print(i)
# 9.Создать список с тремя значениями 'to-delete' и нескольми любыми другими, удалить из него все значения 'to-delete'
to_del = ['to-delete', 123, str, float, 'to-delete', 'something', [1, 2, 3, 4, 5], 'to-delete']
new_del = [item for item in to_del if item != 'to-delete']
print(new_del)
# 10.Пройти по всем числам от 1 до 10 в обратную сторону (то есть: от 10 до 1), напечатать их в консоль
for number in range(10, 0, -1):
    print(number)

