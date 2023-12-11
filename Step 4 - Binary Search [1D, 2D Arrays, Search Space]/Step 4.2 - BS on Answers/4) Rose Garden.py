#https://www.codingninjas.com/studio/problems/rose-garden_2248080?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from typing import List

def roseGarden(arr: List[int], r: int, b: int):
     n=len(arr)

    # border case

    if r * b > n:

        return -1



    days = 1



    while 1:


        # Initialize 'cntR' and 'cntB' to store consequtive roses found and bouquets respectively

        cntR, cntB = 0, 0


        # Greedily find subarrays of size eqal to 'R'

        for i in range(n):


            # Check if current element in less than or equal to 'mid'

            if arr[i] <= days:

                cntR += 1

            else:

                cntR = 0


            # Found 'R' consequetive bloomed flowers

            if cntR == r:

                cntB += 1

                cntR = 0


        # Found the optimal anser

        if cntB >= b:

            return days


        # Check for the next day

        days += 1

    # Finally return the answer

    return days