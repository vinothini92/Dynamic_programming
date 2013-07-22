def matrix_chain_order(p):
    n = len(p)-1
    m = [[0 for j in range(0,n+1)] for i in range(0,n+1)]
    s = [[0 for j in range(0,n+1)] for i in range(0,n)]
    for i in range(1,n+1):
        m[i][j] = 0
    for l in range(2,n+1):
        for i in range(1,n-l+2):
            j = i+l-1
            m[i][j] = 1000000
            for k in range(i,j):
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    
    return m,s

def print_parens(s,i,j):
    if i == j:
        print "A%d"%i,
    else:
        print "(",
        print_parens(s,i,s[i][j])
        print_parens(s,s[i][j]+1,j)
        print ")",

if __name__ == '__main__':
    p = [30,35,15,5,10,20,25]
    n = len(p)
    m,s = matrix_chain_order(p)
    for i in range(1,n):
        for j in range(1,n):
            print "%8d"%(m[i][j]),
        print ""
    print "\ns: "
    for i in range(1,n-1):
        for j in range(1,n):
            print "%8d"%(s[i][j]),
        print ""
    print "\ns: "
    print_parens(s,1,n-1)
    print "\nThe number of multiplications is: %d\n\n"%(m[1][n-1])
        
    
    
