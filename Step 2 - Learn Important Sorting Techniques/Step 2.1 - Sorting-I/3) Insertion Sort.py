#https://www.codingninjas.com/studio/problems/insertion-sort_624381?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
import os
import sys
from copy import deepcopy
input = lambda: sys.stdin.readline().rstrip("\r\n")
sys.setrecursionlimit(10 ** 7)
def insertionSort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp





    
        
class Runner:
    def __init__(self):
        self.n = 0
        self.arr =[]

    def takeInput(self):
        self.n = int(input())
        self.arr= list(map(int, input().split()))

    def execute(self):

        ans = insertionSort(self.arr)

    def executeAndPrintOutput(self):
        ans = insertionSort(self.arr)
        print(*self.arr)

runner = Runner()
runner.takeInput()
runner.executeAndPrintOutput()