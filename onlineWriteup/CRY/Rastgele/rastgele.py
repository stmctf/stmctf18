# https://pypi.org/project/pycryptodomex/
from Crypto.Util.number import isPrime
# https://pypi.org/project/pycryptodomex/
from Crypto.Random.random import getrandbits
from GIZLI import FLAG
import math
import binascii


def nextPrime(p):
    if p % 2 == 0:
        p += 1
    else:
        p += 2
    while not isPrime(p):
        p += 2
    return p


def encrypt():
    r = getrandbits(1024)
    p = nextPrime(r + 2 * int(math.sqrt(r)))
    q = nextPrime(5 * r + 3 * int(math.sqrt(p) + int(math.log(r))))

    n = p * q
    e = 0x10001

    m = int(binascii.hexlify(FLAG.encode('utf-8')), 16)
    c = pow(m, e, n)
    return n, hex(c)[2:]


if __name__ == '__main__':
    print(encrypt())
