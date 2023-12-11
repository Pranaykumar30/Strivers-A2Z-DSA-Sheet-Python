#https://www.codingninjas.com/studio/problems/binary-search_972?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def search(nums: [int], target: int):
    # write your code logic !!
    lower = 0
    higher = len(nums) - 1

    while lower <= higher:
        mid = lower + (higher - lower) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lower = mid + 1
        else:
            higher = mid - 1

    return -1




    
n= int (input())
arr = list(map(int,input().strip().split()))[:n]
target =int (input())
print (search(arr, target))