#Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
#Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.

def arithmetic_progression(one_element, difference, quantity_element):
    array = []
    for i in range(quantity_element):
        array.append(one_element + i * difference)
    return array

one_element = int(input("Введите первый элемент: "))
difference = int(input("Введите разность прогрессии: "))
quantity_element = int(input("Введите количество элементво: "))

array = arithmetic_progression(one_element, difference, quantity_element)

print("Массив элементов:")
for element in array:
    print(element)

