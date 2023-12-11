#https://www.codingninjas.com/studio/problems/square-root-integral_893351?leftPanelTab=0%3Futm_source%3Dstriver&utm_medium=website&utm_campaign=a_zcoursetuf
def floorSqrt(n):
   ans = 1
   while ans <= (n // ans):
      ans += 1
   return ans - 1
n= int(input())
print(floorSqrt(n))