import numpy as np


def find_key(p, c):
    inv_p = np.linalg.inv(p)

    n = 0
    k = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])

    assigned_index = []
    while n < 1000:
        product = np.dot(31 * n + c, inv_p)
        for index_row, row in enumerate(product):
            for index_col, col in enumerate(row):
                if (index_row, index_col) not in assigned_index:
                    if abs(round(col) - col) < 0.0000000001:
                        k[index_row][index_col] = col
                        assigned_index.append((index_row, index_col))

        if n < 0:
            n = abs(n) + 1
        elif n > 0:
            n *= -1
        else:
            n += 1
    return k


def decrypt(c, k):
    inv_k = np.linalg.inv(k)
    product = np.dot(inv_k, c)
    p = np.array([[0], [0], [0], [0]])

    for index_row, row in enumerate(product):
        # for index_col, col in enumerate(row):
            p[index_row] = row % 31

    return p

def main():
    p = np.array([[2, 2, 7, 15], [19, 0, 14, 6], [17, 15, 12, 20], [11, 18, 4, 15]])
    c = np.array([[7, 6, 15, 15], [7, 14, 5, 11], [19, 19, 18, 8], [3, 0, 2, 17]])
    k = find_key(p, c)
    print(k)

    cipher_string = '!LPUMYAIJ?.MPA.DVRFUTNRUZYEFM?QVKJTOBTDRIAN!?SLQBKESZOSFRAAWYPI.VBOLLMWAWEMQ.JYBOITGNJRIFYGEGIBC?RB?UN?MORI,'
    cipher_num_list = []

    for char in cipher_string:
        if char.isalpha():
            cipher_num_list.append(ord(char) - 65)
        elif char == ',':
            cipher_num_list.append(26)
        elif char == '.':
            cipher_num_list.append(27)
        elif char == '?':
            cipher_num_list.append(28)
        elif char == '!':
            cipher_num_list.append(29)
        elif char == ' ':
            cipher_num_list.append(30)

    plain_num_list = []
    plain_string = ''

    i = 0
    while i < len(cipher_string):
        plain_num_array = decrypt(cipher_num_list[i:i+len(p)], k)
        plain_num_list += np.ndarray.tolist(plain_num_array)
        i += len(p)

    for num in plain_num_list:
        if 0 <= num[0] <= 25:
            plain_string += (chr(num[0] + 65))
        elif num[0] == 26:
            plain_string += ','
        elif num[0] == 27:
            plain_string += '.'
        elif num[0] == 28:
            plain_string += '?'
        elif num[0] == 29:
            plain_string += '!'
        elif num[0] == 30:
            plain_string += ' '

    print(plain_string)

if __name__ == '__main__':
    main()
