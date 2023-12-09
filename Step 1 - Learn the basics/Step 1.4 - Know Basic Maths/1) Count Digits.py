#https://www.codingninjas.com/studio/problems/count-digits_8416387?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def countDigits(n: int) -> int:
    count = 0
    for digit in str(n):
        if int(digit) != 0 and n % int(digit)==0:
            count += 1
    return count
