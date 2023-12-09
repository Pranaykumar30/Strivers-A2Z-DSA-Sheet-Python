#https://www.codingninjas.com/studio/problems/reverse-bits_2181102?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def reverseBits(n):
    reversed_bits = 0
    for i in range (32):
        reversed_bits <<= 1
        is_bit_set = 1 if (n & (1 << i)) != 0 else 0
        reversed_bits |= is_bit_set
    return reversed_bits
