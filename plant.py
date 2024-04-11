from rsa import decrypt,pub1,encrypt


resolution = 1

A = [[1,0.25],[0.4,0]]
x = [0,1]


def ord_mul(A,x):

    n = len(A)
    m = len(A[0])
    res = [0]*n
    for i in range(n):
        for j in range(m):
            res[i] += A[i][j]*x[j]
    return res



def num2int(A):
    n = len(A)
    m = len(A[0])
    res = [[0]*m for _ in range(n)] 
    for i in range(n):
        for j in range(m):
            if A[i][j] >= 0:
                res[i][j] = round(A[i][j]*resolution)
            else:
                res[i][j] = round(A[i][j]*resolution)+pub1

    return res



def int2num(A,myres=resolution):
    n = len(A)
    m = len(A[0])
    res = [[0]*m for _ in range(n)] 

    for i in range(n):

        for j in range(m):
            if A[i][j] <= pub1//2:
                res[i][j] = A[i][j]/myres
            else:
                res[i][j] = (A[i][j]-pub1)/myres
    return res






def encrypt_mat(A):
    n = len(A)
    m = len(A[0])
    res = [[0]*m for _ in range(n)] 
    B = num2int(A)
    for i in range(n):
        for j in range(m):
            res[i][j] = encrypt(B[i][j])

    return res 



def decrypt_mat(A,myres=resolution):
    n = len(A)
    m = len(A[0])
    res = [[0]*m for _ in range(n)] 
    for i in range(n):
        for j in range(m):
            res[i][j] = decrypt(A[i][j])

    return int2num(res,myres) 


def sai2vec(mysai):
    B = decrypt_mat(mysai,resolution**2)
    n = len(B)
    m = len(B[0])
    res = [0]*n
    for i in range(n):
        for j in range(m):
            res[i] += B[i][j]

    return res

def print_mat(A,Ehex=False):
    for r in A:
        for c in r:
            if Ehex:
                print(hex(c),end =" ")
            else:
                print(c,end=" ")
        print()





# M = encrypt_mat(A)
# D = decrypt_mat(M)

# print_mat(A)
# print_mat(M,True)
# print_mat(D)


# A_enc = encrypt_mat(A)
# x_enc = encrypt_mat([x])[0]

# mysai = sai(A_enc,x_enc)
# ans = sai2vec(mysai)

# print(ord_mul(A,x))
# print(ans)