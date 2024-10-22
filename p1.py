from find_max_first_element_podspiski import *
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

main()
