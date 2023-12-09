#https://www.codingninjas.com/studio/problems/-print-n-times_8380707?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from  typing import *

def printNtimes(n: int) -> None:
    print("Coding Ninjas", end=" ")
    if n > 1:
        printNtimes(n-1)
