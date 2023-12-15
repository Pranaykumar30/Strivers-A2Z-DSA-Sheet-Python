#https://www.codingninjas.com/studio/problems/good-numbers_625508?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from typing import List
def goodWithoutDigit(n: int, digit: int) -> bool:
    # Check if the last digit of 'n' is equal to 'digit'.
    if n % 10 == digit:
        return False
    
    # Calculate the sum of digits and compare it with the last digit of 'n'.
    total_sum = n % 10
    n = n // 10
    
    while n > 0:
        # If any digit is equal to 'digit' or less than or equal to the total sum,
        # the number is not considered "good".
        if n % 10 == digit or n % 10 <= total_sum:
            return False
        
        # Update the total sum by adding the current digit.
        total_sum += n % 10
        n = n // 10
    
    return True

def goodNumbers(a: int, b:int, digit:int) -> List[int]:
    ans = []
    
    # Iterate through the range from 'a' to 'b'.
    for i in range(a, b+1):
        # Check if the current number is "good" without the specified 'digit'.
        if goodWithoutDigit(i, digit):
            # If the number is "good", add it to the answer list.
            ans.append(i)
    
    return ans