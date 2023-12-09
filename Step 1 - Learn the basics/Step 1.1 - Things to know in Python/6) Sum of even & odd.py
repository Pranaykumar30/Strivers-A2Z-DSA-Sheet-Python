#https://www.codingninjas.com/studio/problems/sum-of-even-odd_624650?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

## Note : For printing multiple values in one line, put them inside print separated by space.
## You can follow this syntax for printing values of two variables val1 and val2 separaetd by space -
## print(val1, " ", val2)
n = int(input())
es = 0
os = 0
while n >0:
    last = n%10
    if last%2 == 0:
        es +=last
    else:
        os +=last
    n = n//10
print(es, "", os)