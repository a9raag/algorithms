def getSum(BITTree, i):
    s = 0
    i += 1
    while i > 0:
        s += BITTree[i]
        i -= i & (-i)
    return s


def updateBit(BITTree, n, i, value):
    i += 1
    while i <= n:
        BITTree[i] += value
        i += i & (-i)


def construct(arr, n):
    BITTree = [0] * (n + 1)

    for i in range(n):
        updateBit(BITTree, n, i, arr[i])
    return BITTree


if __name__ == '__main__':
    freq = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
    BITTree = construct(freq, len(freq))
    print(getSum(BITTree, len(freq)-1))
