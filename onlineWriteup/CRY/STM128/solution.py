import stm128
faulty_hash="c87cced0b2430495ea3900129da1f2aa"
rev_sbox = [0] * 256
rev_p = [0] * 16

def reverse_permutation(data):
    temp = bytearray([0]) * 16
    for i in range(len(temp)):
        temp[rev_p[i]] = data[i]
    return temp


def reverse_sbox(data):
    for i in range(len(data)):
        data[i] = rev_sbox[data[i]]
    return data


def main():
    for i in range(len(rev_sbox)):
        rev_sbox[stm128.sbox[i]] = i
    for i in range(len(rev_p)):
        rev_p[stm128.p[i]] = i
    hash = bytearray(stm128.int_to_bytes(int(faulty_hash, 16)))
    last_roundkey = stm128.pad(bytearray(",".encode('ascii')))
    for i in range(stm128.round):
        hash = reverse_permutation(hash)
        hash = reverse_sbox(hash)
        hash = stm128.repeated_xor(hash, last_roundkey)
    hash = hex(stm128.bytes_to_int(hash))[2:]

    print("soruda verilen deger: ",faulty_hash)
    print("hesaplanan deger: ",hash)

if __name__ == '__main__':
    main()
