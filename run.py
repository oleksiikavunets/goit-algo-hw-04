import random
import string
import timeit


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


l1 = [random.randint(1, 100) for _ in range(100)]
l2 = [random.randint(1, 1000) for _ in range(1000)]
l3 = [random.randint(1, 10000) for _ in range(10000)]
l4 = [random.randint(1, 100000) for _ in range(100000)]

chars = (string.ascii_letters.lower() + string.ascii_letters.upper() + string.digits)

a1 = [random.choice(chars) for _ in range(100)]
a2 = [random.choice(chars) for _ in range(1000)]
a3 = [random.choice(chars) for _ in range(10000)]
a4 = [random.choice(chars) for _ in range(100000)]

print('\nSORT LIST OF INTS\n')

for ls in (l1, l2, l3, l4):
    print(f'\n{len(ls)} ELEMENTS:')
    t_s = timeit.timeit(lambda: sorted(ls), number=1)
    print(f'Tim Sort:      ', t_s)

    m_s = timeit.timeit(lambda: merge_sort(ls), number=1)
    print(f'Merge Sort:    ', m_s)

    i_s = timeit.timeit(lambda: insertion_sort(ls), number=1)
    print(f'Insertion Sort:', i_s)

    print('=' * 20)

print('\nSORT LIST OF CHARS\n')

for ls in (a1, a2, a3, a4):
    print(f'\n{len(ls)} ELEMENTS:')

    t_s = timeit.timeit(lambda: sorted(ls), number=1)
    print(f'Tim Sort:      ', t_s)

    m_s = timeit.timeit(lambda: merge_sort(ls), number=1)
    print(f'Merge Sort:    ', m_s)

    i_s = timeit.timeit(lambda: insertion_sort(ls), number=1)
    print(f'Insertion Sort:', i_s)

    print('=' * 20)
