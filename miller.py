import random
import sys
sys.setrecursionlimit(10**5) 

prime_list = []
N = 10000 # probablity of number being composite after passing test is 4^-pi(N)

def prime_check(n):
    if n <= 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True



for i in range(N):
    if prime_check(i):
        prime_list.append(i)


def pow(a, n, mod):
    if n == 0:
        return 1
    mya = pow(a, n // 2, mod)
    d = (mya*mya)%mod
    if n % 2 == 1:
        d = (d*a)%mod
    return d

def prime(n):
    if n <= N:
        return prime_check(n)
    d = n - 1
    while d % 2 == 0:
        d //= 2
    cnt = 0
    for a in prime_list:
        k = d
        check = False
        if pow(a, k, n) == 1:
            cnt += 1
            check = True
        while k <= n:
            if pow(a, k, n) == n - 1:
                cnt += 1
                check = True
                break
            k *= 2
        if not check:
            return False
    return True if cnt == len(prime_list) else False




def random_number(k,base = 10):
    a = 0
    for i in range(k):
        r = random.randint(0,base-1)
        if i == 0:
            r = random.randint(1,base-1)
        a *= base
        a += r
    return a




def find_prime(min,max):
    
    for number in range(min,max):

        if number % 5*10**9 == 0:
            print('#',end='',flush=True)


        if not number&1:
            continue

        if prime(number):
            print()
            return number

    return -1

def main():

    number_of_digit = 512
    min = random_number(number_of_digit,2)
    max = min+random_number(11)
    num1 = find_prime(min,max)
    min = random_number(number_of_digit,2)
    max = min+random_number(11)
    num2 = find_prime(min,max)

    with open("prime.txt", "w") as file:
        file.write("p = "+str(num1)+"\nq = "+ str(num2))
        print()
        print("prime number saved in prime.txt")


if __name__ == "__main__":
    main()