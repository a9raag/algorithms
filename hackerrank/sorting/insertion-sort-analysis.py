from collections import defaultdict


def getSum(BITree, i):
    s = 0
    i += 1
    while i > 0:
        s += BITree[i]
        i -= i & (-i)
    return s


def jq(data, i, size):
    j, s = i, 0
    while i > 0:
        s += data[i]
        i -= i & -i
    while j < size:
        data[j] += 1
        j += j & -j
    print(data)
    return s


def test2(arr):
    size = 10000001
    bit = defaultdict(int)
    bit_sum = 0
    count = 0
    for n in arr:
        count += bit_sum
        idx = n
        while idx:
            count -= bit[idx]
            idx -= idx & -idx

        idx = n
        while idx < size:
            bit[idx] += 1
            idx += idx & -idx

        bit_sum += 1
    return count


def test1(arr):
    size = len(arr) + 1
    data = size * [0]
    r = [i - jq(data, v, size) for i, v in enumerate(arr)]
    s = sum(r)
    print(r)
    print(data)
    return s


def updateBit(BITree, n, i, value):
    i += 1
    while i <= n:
        BITree[i] += value
        i += i & (-i)


def construct(arr, n):
    BITree = [0] * (n + 1)
    for i in range(n):
        updateBit(BITree, n, i, arr[i])

    return BITree


def read_single(BITree, i):
    z = i - (i & -i)
    y = i - 1
    s = BITree[i]
    while y != z:
        s -= BITree[y]
        y -= y & -y
    return s


if __name__ == '__main__':
    arr = [2, 1, 3, 1, 2]
    # arr = [4]*5
    arr = [4, 3, 2, 1]
    BITree = construct(arr, len(arr))
    # print(getSum(BITree, len(arr) - 1))
    # print(BITree)
    # print(read_single(BITree, 2))
    print(test2(arr))
