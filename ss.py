import numpy as np

class StateSpace :

    def __init__(self,A,B,C,D,initial_value=None):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.n,_ = A.shape
        if initial_value is None:
            self.initial_value = np.zeros((self.n,1))
        else:
            self.initial_value = initial_value
        self.x = self.initial_value
    
    def reset(self):
        self.x = self.initial_value
    
    def out(self,r):
        y = self.C @ self.x + self.D * r
        self.x = self.A @ self.x + self.B * r
        return y[0,0]


    def sim(self,input):
        output = []
        x = self.initial_value
        for r in input:
            x = self.A @ x+ self.B * r
            y = self.C @ x
            output.append(y[0,0])

        return output 


    

class MED: #matrix encode decode
    
    def __init__(self,n,scale_factor):
       self.n = n
       self.scale_factor = scale_factor

    
    def decode(self,A,iteration=1):
        if np.isscalar(A):
            res = ((A+self.n//2)%self.n)-self.n//2
            res /= (self.scale_factor**iteration)
            return res
        
        N = len(A)
        M = len(A[0])
        Adecode = np.zeros((N,M))
        for i in range(N):
            for j in range(M):
                Adecode[i,j] =  ((A[i][j]+self.n//2)%self.n)-self.n//2
                Adecode[i,j] /= (self.scale_factor**iteration)
        return Adecode

    def encode(self,A,iteration=1):
        if np.isscalar(A):
            res = int(A*self.scale_factor**iteration)
            if A < 0:
                res +=self.n
            return res
                
        N,M = A.shape
        Aencode = [[0]*M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                Aencode[i][j] = int(A[i,j]*self.scale_factor**iteration)
                if Aencode[i][j] < 0:
                    Aencode[i][j] += self.n
        return Aencode



    
    
