def average(mass, size):
    summ = 0
    i = 0
    while i < size:
        summ = summ + mass[i]
        i = i + 1
    aver = summ / size
    return aver


def minimum1(mass, size):
    min1 = mass[0]
    i = 1
    while i < size:
        if min1 > mass[i]:
            min1 = mass[i]
        i = i+1
    return min1


a = [1, 2, 3, 4, 5, 6, 7]
b = minimum1(a, 7)
print("minimum =", b)
c = average(a,7)
print("average =", c)