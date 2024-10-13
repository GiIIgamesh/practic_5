import random
def generate_sublists(length, num_sublists):
    """Генерирует список подсписков заданной длины с случайными числами."""
    sublists = []
    for _ in range(num_sublists):
        sublist = [random.randint(1, 100) for _ in range(length)]
        sublists.append(sublist)
    return sublists
def find_max_first_element_sublist(sublists):
    """Находит подсписок с максимальным первым элементом."""
    max_sublist = None
    max_first_element = float('-inf')
    for sublist in sublists:
        first_element = sublist[0]
        if first_element > max_first_element:
            max_first_element = first_element
            max_sublist = sublist
    return max_sublist
def main():
    length = int(input("Введите длину подсписков: "))
    num_sublists = int(input("Введите количество подсписков: "))
    sublists = generate_sublists(length, num_sublists)
    print("Сгенерированные подсписки:")
    for sublist in sublists:
        print(sublist)
    result_sublist = find_max_first_element_sublist(sublists)
    print("\nПодсписок с максимальным первым элементом:")
    print(result_sublist)
if name == "main":
    main()