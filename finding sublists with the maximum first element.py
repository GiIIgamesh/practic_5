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

main()
def find_max_first_element_podspiski(podspiski):
    """Находит подсписок с максимальным первым элементом."""
    max_podspiski = None
    max_first_element = float('-inf')
    for podspiski in podspiski:
        first_element = podspiski[0]
        if first_element > max_first_element:
            max_first_element = first_element
            max_podspiski = podspiski
    return max_podspiski
def smain():
    for podspiski in podspiski:
        result_podspiski = find_max_first_element_podspiski(podspiski)
        if name == "smain":
            smain()