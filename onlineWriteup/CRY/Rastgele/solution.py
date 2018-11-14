from Crypto.Util.number import inverse
import binascii
import math
from Crypto.Util.number import isPrime
import time

n = 6372770546496319102179620437307638173638450624706994013150556737556325599703330944379292690861019317896179238639531103215452528829844474367267311641005420236669484549925277976322608347329839738367472716421549441841809205650965622561195036563462678859216423865852610719120951177139295537080439411028696345435214848494163374918999689909835436773514063023408641642730779603935834213337924666184669534359324246716927163328942404372033668897126060617824416978557501665796292712890480413460846730640731379072921121900697734892519479348366220299821848153550069772424968362100343986833830629806781246764199433828997536664737
c = int('312a9507b4e1d48cf52c31e9eaf5a044d99b5c14298245ec61c27a0d5e8cfda840e397ab46cc9196a65258debb26c5c96bb23443c94e6bcfd55154f3f14453994e230c2ab106025d7916c9f00a0542bbe1e9c29c0b9620c34f71064f6741a2a7369355fc7bac7dbf1a17142a65855be33076a98e9defd4a48305883abf2d26c424f3b376d6bb8a46112e6a5503b9f787cc2e6eb9746afd083772f7dc5e547efbf1290c3a95dca18d9bb2f0a0d60ce3fc82b4d4e635e2a6b7308d46c09976123c3a1f89823275a945345aa4c311fde2133e8ffbed57ff7ecb9d9415609fb946420e639e95c2fb104810a087d67f2a496ee368b5c929c9ce6998ba581504cc4e25', 16)
e = 0x10001


def nextPrime(p):
    if p % 2 == 0:
        p += 1
    else:
        p += 2
    while not isPrime(p):
        p += 2
    return p


def calculate_n(r):
    p = nextPrime(r + 2 * int(math.sqrt(r)))
    q = nextPrime(5 * r + 3 * int(math.sqrt(p) + int(math.log(r))))
    return p * q


def binary_search(MIN, MAX, r):
    global n
    while MIN < MAX:
        print(r)
        n_ = calculate_n(r)
        if n_ == n:
            return r
        if n_ < n:
            MIN = r + 1
            r = (MAX + r) // 2
        else:
            MAX = r - 1
            r = (MIN + r) // 2
    return -1


def solve():
    r = binary_search(1, 2**1024, 2**512)
    assert r != -1
    p = nextPrime(r + 2 * int(math.sqrt(r)))
    q = nextPrime(5 * r + 3 * int(math.sqrt(p) + int(math.log(r))))
    return p, q


start_time = time.asctime(time.localtime(time.time()))
print(start_time)
p, q = solve()

phi = (p - 1) * (q - 1)

d = inverse(e, phi)
m = pow(c, d, n)
m = binascii.unhexlify(hex(m)[2:])
print(m)
print(start_time)
print(time.asctime(time.localtime(time.time())))
