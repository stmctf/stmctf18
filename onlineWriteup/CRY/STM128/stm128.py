sbox = [166, 6, 104, 67, 182, 132, 211, 93, 230, 52, 224, 141, 131, 92, 207, 216, 231, 138, 219, 127, 156, 66, 163, 41, 112, 10, 57, 119, 61, 32, 250, 158, 154, 157, 115, 151, 164, 255, 125, 135, 118, 215, 111, 183, 117, 133, 73, 173, 2, 176, 189, 147, 242, 121, 17, 221, 208, 145, 196, 188, 155, 34, 159, 38, 202, 213, 25, 42, 184, 103, 241, 129, 45, 20, 59, 253, 243, 102, 168, 79, 91, 113, 21, 206, 185, 37, 90, 70, 245, 62, 223, 8, 108, 49, 130, 97, 12, 217, 4, 146, 136, 3, 47, 204, 234, 180, 228, 82, 197, 240, 110, 218, 247, 160, 120, 214, 39, 212, 232, 81, 194, 246, 105, 40, 162, 89, 94, 50, 5, 123, 139, 43, 175, 193, 85, 116, 53, 109, 128, 165, 179, 251, 144, 16, 201, 222, 83, 181, 244, 29, 149, 124, 78, 174, 14, 77, 190, 150, 96, 26, 142, 18, 187, 80, 72, 225, 114, 58, 88, 1, 9, 143, 27, 178, 46, 192, 161, 65, 172, 152, 95, 233, 23, 210, 200, 249, 106, 13, 64, 199, 254, 56, 209, 48, 15, 51, 54, 30, 167, 229, 186, 87, 137, 11, 19, 36, 60, 28, 63, 126, 237, 35, 0, 205, 226, 31, 55, 227, 170, 76, 238, 191, 195, 74, 98, 248, 68, 252, 100, 69, 101, 236, 198, 44, 84, 7, 71, 153, 33, 134, 22, 177, 86, 107, 171, 203, 169, 235, 75, 24, 220, 148, 140, 239, 122, 99]
p = [15, 10, 0, 6, 7, 9, 1, 13, 12, 11, 4, 3, 2, 5, 8, 14]
round = 16


def pad(data, size = 16):
    pad_byte = (size - len(data) % size) % size
    data = data + bytearray([pad_byte]) * pad_byte
    return data


def repeated_xor(p, k):
    return bytearray([p[i] ^ k[i % len(k)] for i in range(len(p))])


def bytes_to_int(xbytes):
    return int.from_bytes(xbytes, 'big')


def int_to_bytes(x):
    return x.to_bytes(16, 'big')


def group(input, size = 16):
    return [input[i * size: (i + 1) * size] for i in range(len(input) // size)]


def stm128_hash(data):
    state = bytearray([27, 182, 84, 59, 45, 235, 36, 28, 74, 71, 35, 26, 62, 49, 77, 57])
    data = pad(data, 16)
    data = group(data)
    for roundkey in data:
        for _ in range(round):
            state = repeated_xor(state, roundkey)
            for i in range(len(state)):
                state[i] = sbox[state[i]]
            temp = bytearray(16)
            for i in range(len(state)):
                temp[p[i]] = state[i]
            state = temp
    return hex(bytes_to_int(state))[2:]


def main():
    data = input("Hashini hesaplamak istediğiniz stringi giriniz: ")
    data = bytearray(data.encode('ascii'))
    print(stm128_hash(data))


if __name__ == '__main__':
    main()
