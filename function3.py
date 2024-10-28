import statistics

def sort_by_mean(podspiski):
    means = []
    for lst in podspiski:
        mean = statistics.mean(lst)
        means.append((mean, lst))
    means.sort()
    return [x[1] for x in means]