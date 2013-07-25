#5*5 checker board problem

def max_cost(a,n):
    max = 0
    cost = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        cost[n-1][i] = a[n-1][i] 
    for i in range(n-2,-1,-1):
        for j in range(n):
            cost[i][j] = a[i][j] + max_pro(cost,i,j,n)
    for i in range(n):
        if max < cost[0][i]:
            max = cost[0][i]
    print "maximum cost=",max
    print "Cost Table:"     
    for i in range(n):
        for j in range(n):
            print "%8d"%(cost[i][j]),
        print ""
    print "\n"
 

def max_pro(rs,i,j,n):
    if j==0 :
        if rs[i+1][j] > rs[i+1][j+1]:
            return rs[i+1][j]
        else:
            return rs[i+1][j+1]
    elif j==n-1:
        if rs[i+1][j]>rs[i+1][j-1]:
            return rs[i+1][j]
        else:
            return rs[i+1][j-1]
    else:
        if rs[i+1][j]>rs[i+1][j-1]:
            max = rs[i+1][j]
        else:
            max = rs[i+1][j-1]
        if max>rs[i+1][j+1]:
            return max
        else:
            return rs[i+1][j+1]

if __name__ == '__main__':
    a = [[3,-6,5,7,42],[24,-20,41,84,-50],[56,-54,5,-25,8],[5,74,10,8,45],[-9,-21,12,62,4]]
    n = len(a)
    max_cost(a,n)
