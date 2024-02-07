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


def get_hexa(n):
    hex_digits = "0123456789ABCDEF"
    hex_string = ""
    for char in n:
        decimal_value = ord(char)
        hex_value = ""
        while decimal_value > 0:
            remainder = decimal_value % 16
            hex_value = hex_digits[remainder] + hex_value
            decimal_value = decimal_value // 16
        hex_string += hex_value
    
    print(hex_string)
    return hex_string




get_hexa("13")



def get_decimal(n):
    list = { '0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15 }
    decimal = 0
    for i in range(len(n)):
        decimal += list[n[i]] * (16 ** (len(n)-i-1))
    print(decimal)
    return decimal
get_decimal("1EC56A")


def string_to_binaire(n):
    decimal = int(n)
    binary = bin(decimal)[2:]
    print(binary)
    return binary


string_to_binaire("15")