#https://www.codingninjas.com/studio/problems/palindrome-number_624662?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
n=int(input())  
# taking n as a input 
## write your code !!
temp = n
rev = 0
while(n > 0):
    dig = n % 10
    rev = rev*10+dig
    n = n//10
if (temp==rev):
    print("true")
else:
    print("false")
