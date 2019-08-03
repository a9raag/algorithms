import os


def quickSort(arr):
    pivot = arr[0]
    pivot_index = -1
    for i in range(len(arr)):

        if arr[i] <= pivot:
            pivot_index += 1
            arr[i], arr[pivot_index] = arr[pivot_index], arr[i]
    arr[0], arr[pivot_index] = arr[pivot_index], arr[0]
    return arr


def n_input_str():
    return "5"


def arr_input_str():
    return "4 5 3 7 2"


if __name__ == '__main__':
    n = int(n_input_str())

    arr = list(map(int, arr_input_str().rstrip().split()))

    result = quickSort(arr)

    print(' '.join(map(str, result)))
    print('\n')

    print()
