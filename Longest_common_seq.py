
def Lcs(seq1, seq2):
    m = len(seq1)
    n = len(seq2)
    print "Length of First Seq = %d"%m
    print "Length of Second Seq = %d"%n
    lcs = [[0] * (n+1) for i in range(m+1)]
    ptr = [[(0, 0)] * (n+1) for i in range(m+1)]
    x = (0, 0)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
                ptr[i][j] = (i - 1, j - 1)   
            elif lcs[i][j - 1] > lcs[i - 1][j]:
                lcs[i][j] = lcs[i][j - 1]
                ptr[i][j] = (i, j - 1)  
            else:
                lcs[i][j] = lcs[i - 1][j]
                ptr[i][j] = (i - 1, j) 
            if lcs[i][j] > lcs[x[0]][x[1]]:
                x = (i, j)

    return lcs, ptr,x


def printRev(lcs, ptr,x):
    if x != (0, 0):
        printRev(lcs, ptr, ptr[x[0]][x[1]])
        if (x[0] == ptr[x[0]][x[1]][0] + 1 and x[1] == ptr[x[0]][x[1]][1] + 1):
            print(seq1[x[0] - 1])

if __name__ == '__main__':
    seq1 = "BDCABA"
    seq2 = "ABCBDAB"
    lcs, ptr,x = Lcs(seq1, seq2)
    n = len(lcs)
    print "Length of common subsequence =",lcs[n-1][n-1]
    print "LCS pair:"
    printRev(lcs, ptr,x)
