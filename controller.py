from rsa import mul

def sai(A,x):
    n = len(A)
    m = len(A[0])
    res = [[0]*m for _ in range(n)] 
    for i in range(n):
        for j in range(m):
            res[i][j] = mul(A[i][j],x[j])

    return res