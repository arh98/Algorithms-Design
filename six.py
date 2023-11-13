import random

# Ahmadreza hafizi - 9612762912
# greedy algorithms - week 6

def generate(m, n):
    return [random.randint(1, m) for _ in range(n)]


def two_smallest(mybars):
    bars = mybars.copy()
    bars.sort()
    total_cost = 0
    current_cost = 0
    while len(bars) > 1:
        first = bars.pop(0)
        second = bars.pop(0)
        current_cost = first + second
        # print(current_cost , total_cost)
        # new bar = current_cost or (fir + sec)
        bars.insert(0, current_cost)
        total_cost = current_cost + total_cost
    print(total_cost)
    # return bars[0]


def two_largest(mybars):
    bars = mybars.copy()
    bars.sort(reverse=True)
    total_cost = 0
    current_cost = 0
    while len(bars) > 1:
        first = bars.pop(0)
        second = bars.pop(0)
        current_cost = first + second
        bars.insert(0, current_cost)
        total_cost = current_cost + total_cost
    print(total_cost)
    # return bars[0]


def next_one_smallest(mybars):
    pass


def random_orders(mybars):
    bars = mybars.copy()
    total_cost = 0
    current_cost = 0
    while len(bars) > 1:
        first = bars.pop(0)
        second = bars.pop(0)
        current_cost = first + second
        bars.insert(0, current_cost)
        total_cost = current_cost + total_cost
    print(total_cost)
    # return bars[0]


def fixed_cost(bars):
    total_cost = 0
    fixed_cost = 1000
    while len(bars) > 1:
        first = bars.pop(0)
        second = bars.pop(0)
        bars.insert(0, first + second)
        total_cost = fixed_cost + total_cost
    print(total_cost)
    # return bars[0]
# sortedd = [1,2,5]
# rev_sorted = [5,2,1]
# randomedd = [2,5,1]


test_case = generate(1000, 100000)
two_smallest(test_case)
two_largest(test_case)
random_orders(test_case)
fixed_cost(test_case)
