import sys
import random
sys.setrecursionlimit(10**5)


p = 6936318504396482717943727120074606196109
q = 6826171487594198971240406686985297766887

def pow(a, n, mod):
    if n == 0:
        return 1
    mya = pow(a, n // 2, mod)
    d = (mya*mya)%mod
    if n % 2 == 1:
        d = (d*a)%mod
    return d



def gcd(a,b):
    if b == 0:
        return 1,0,a

    x1,y1,g = gcd(b,a%b)
    return y1,x1-y1*(a//b),g


def public_key():
    a = 2**15
    phi_n = (p-1)*(q-1)
    _,_,d = gcd(a,phi_n) 
    while d != 1:
        a = random.randint(2**14,2**15)
        _,_,d = gcd(a,phi_n)
    return (p*q,a)


def private_key(e):
    phi_n = (p-1)*(q-1)
    ep,_,_ = gcd(e,phi_n)
    return (ep+phi_n)%phi_n




n,e = public_key()
pub1 = n
ep = private_key(e)

print(hex(n))
print(hex(e))
print(hex(ep))


def encrypt(m,pub1=n,pub2=e):
    return pow(m,pub2,pub1)

def decrypt(c,pv1=ep,pub1=n):
    return pow(c,pv1,pub1) 


def string_to_number(s):
    return int.from_bytes(s.encode(), 'big')

def number_to_string(num):
    return num.to_bytes((num.bit_length() + 7) // 8, 'big').decode()

def mul(a,b):
    return (a*b)%n

def main():
    t1 = "hello"
    tn = string_to_number(t1)
    e1 = encrypt(tn)
    d1 = decrypt(e1)
    print(t1)
    print(hex(e1))
    print(number_to_string(d1))


if __name__ == "__main__":
    main()





