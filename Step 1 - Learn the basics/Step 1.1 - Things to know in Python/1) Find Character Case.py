#https://www.codingninjas.com/studio/problems/find-character-case_58513?utm_source=striver&utm_medium=website&utm_campaign=a_zc
## Read input as specified in the question.
## Print output as specified in the question.
c = input() [0]
if ('a'<= c and c <= 'z'):
    print(0)
elif ('A' <= c and c <= 'Z'):
    print(1)
else:
    print(-1)