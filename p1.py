from finding_sublists_with_the_maximum_first_element import *
from func2 import *
from function3 import *
import random

def main():
    print('Введите длину списка')
    spisok = int(input())
    print('Введите количество подсписков')
    podspicok = int(input())

    random_list = [random.randint(0, 100) for _ in range(spisok)]
    print("Сгенерированный список:", random_list)

    # Разделяем на подсписки
    podspiski = [random_list[i::podspicok] for i in range(podspicok)]

    # Выводим подсписки в одной строке
    print(podspiski)

    print('Выберите действие: ')
    a = int(input())
    if a == 1:
        print(f'{find_max_first_element_podspiski(podspiski)}')
    elif a == 2:
        print(f'{find_max_difference(podspiski)}')
    elif a == 3:
        print(f'{sort_by_mean(podspiski)}')

main()
