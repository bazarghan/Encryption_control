from miller import prime
num = 911996251998911996251998


for i in range(100):
    num *= 10
    if prime(num+1):
        print(num+1)