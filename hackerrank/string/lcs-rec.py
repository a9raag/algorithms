def lcs(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m - 1] == Y[n - 1]:
        print("Endings Match  ", X[:m], Y[:n])
        return 1 + lcs(X, Y, m - 1, n - 1)
    else:
        print("!Endings Match ", X[:m], Y[:n])
        return max(lcs(X, Y, m, n - 1), lcs(X, Y, m - 1, n))


if __name__ == '__main__':
    X = "AGGTAB"
    Y = "GXTXAYB"
    print(lcs(X, Y, len(X), len(Y)))
