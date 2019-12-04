#c must be in nonincreasing order
def make_change(c, target):
    counts = [0] * len(c)
    for i in range(len(c)):
        while target >= c[i]:
            counts[i] += 1
            target -= c[i]
    return counts
