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