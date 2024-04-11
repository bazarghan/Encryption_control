class EncyrptedStateSpace :

    def __init__(self,publick_key,A,B,C,D,initial_value):
        self.g,self.n = publick_key
        self.mod = self.n*self.n
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.initial_value = initial_value
        self.x = initial_value
    
    def pow(self,a, n):
        if n == 0:
            return 1
        mya = pow(a, n // 2, self.mod)
        d = (mya*mya)%self.mod
        if n % 2 == 1:
            d = (d*a)%self.mod
        return d
    
    def reset(self):
        self.x = self.initial_value
    
    def mul(self,A,x):

        if len(A[0]) != len(x):
            raise ValueError("Number of columns in A must be equal to number of rows in x")
    
        result = [[1 for _ in range(len(x[0]))] for _ in range(len(A))]
    
        for i in range(len(A)):
            for j in range(len(x[0])):
                for k in range(len(x)):
                    result[i][j] = (result[i][j]*self.pow(x[k][j],A[i][k]))%self.mod

        return result
    

    
    def sum(self,A,B):
        N = len(A)
        M = len(B[0])
        res = [[0]*M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                res[i][j] = (A[i][j]*B[i][j])%self.mod

        return res
    
    def out(self,r):
        y = self.sum(self.mul(self.C,self.x),self.mul(self.D,[[r]]))
        self.x = self.sum(self.mul(self.A,self.x),self.mul(self.B,[[r]]))
        return y[0][0]



