import random
import sys
from miller import find_prime,random_number
sys.setrecursionlimit(10**5) 



class Encyrptoin:

    def __init__(self,security=256,pre=False):
        if pre:
            self.p = 6736023398256804975611173460210278375247435061689987542430535414463938545072112366107747438457918862839195628606055769668845055591746900055488912456087339
            self.q = 8442353121979374339039759469686625297903401921868308911587130983032512128912182214675493083829037046956252538975545539450098115273542985218698958313283097
        else:
            a = random_number(security,2)
            l = random_number(64,2)
            b = random_number(security,2)
            self.p = find_prime(a,a+l)
            self.q = find_prime(b,b+l) 
        self.keyGen()

    def funcL(self,x,n):
        return (x-1)//n

    def pow(self,a, n, mod):
        if n == 0:
            return 1
        mya = pow(a, n // 2, mod)
        d = (mya*mya)%mod
        if n % 2 == 1:
            d = (d*a)%mod
        return d



    def gcd(self,a,b):
        if b == 0:
            return 1,0,a

        x1,y1,g = self.gcd(b,a%b)
        return y1,x1-y1*(a//b),g



    def lcm(self,a,b):
        _,_,g = self.gcd(a,b)
        return (a*b)//g




    def generateSample(self,n):
        a = 2**16+1
        _,_,d = self.gcd(a,n) 
        while d != 1:
            a = random.randint(1,2**64)
            _,_,d = self.gcd(a,n)
        return a


    def keyGen(self):
        p = self.p
        q = self.q
        lamb = self.lcm(p-1,q-1)
        n = p*q
        g = self.generateSample(n)
        f = self.funcL(self.pow(g,lamb,n*n),n)
        _,_,d = self.gcd(f,n)
        while d != 1:
            g = self.generateSample(n)
            f = self.funcL(self.pow(g,lamb,n*n),n)
            _,_,d = self.gcd(f,n)

        mui,_,_ = self.gcd(f,n)
        self.g = g
        self.n = n
        self.lamb = lamb
        self.mui = mui


    def publicKey(self):
        return self.g,self.n

    def privateKey(self):
        return self.lamb,self.mui


    def encrypt(self,m,pub1=None,pub2=None):
        if pub1 is None:
            pub1 = self.n
        if pub2 is None:
            pub2 = self.g

        n2 = pub1*pub1
        r = random.randint(1,pub1)
        return (self.pow(pub2,m,n2)*self.pow(r,pub1,n2))%n2
    
    def encrypt_mat(self,A):
        result = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(A[0])):
                result[i][j] = self.encrypt(A[i][j])
        return result
    


    def decrypt(self,c,pv1=None,pv2=None,pub1=None):
        if pv1 is None:
            pv1 = self.lamb 
        if pv2 is None:
            pv2 = self.mui
        if pub1 is None:
            pub1 = self.n

        n2 = pub1*pub1
        return (self.funcL(self.pow(c,pv1,n2),pub1)*pv2)%pub1 

    def decrypt_mat(self,A):
        result = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]
        for i in len(A):
            for j in len(A(0)):
                result[i][j] = self.decrypt(A[i][j])
        return result
    


    def string_to_number(s):
        return int.from_bytes(s.encode(), 'big')

    def number_to_string(num):
        return num.to_bytes((num.bit_length() + 7) // 8, 'big').decode()






def main():

    myenc = Encyrptoin()
    a =  5783
    b = -100
    g,n = myenc.publicKey()
    b += n

    b = (b+n)%n
    ae = myenc.encrypt(a)
    be = myenc.encrypt(b)
    n2 = n*n
    res,_,_ = myenc.gcd(ae,n2)
    print(((myenc.decrypt(ae*be)+n//2)%n)-n//2) 
if __name__ == "__main__":
    main()

