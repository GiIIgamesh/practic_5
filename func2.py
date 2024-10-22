from itertools import combinations

def find_max_difference(podspiski):
    max_diff = 0
    max_sublist = None

    for sl in podspiski:
        if not sl:
            continue

        min_value = min(sl)
        max_value = max(sl)
        current_diff = max_value - min_value

        if current_diff > max_diff:
            max_diff = current_diff
            max_sublist = sl

    return max_sublist