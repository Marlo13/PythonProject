'''
module demo: contient une fonction test1
'''
print("Hello, dans demo.py !")

def test1():
    print("Méthode test1 dans demo.py")
    return None

def est_premier(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def couple_premier(n):
    primes = []
    for i in range(2, n-1):
        if est_premier(i) and est_premier(i+2):
            primes.append((i, i+2))
    print(primes)
    return primes
