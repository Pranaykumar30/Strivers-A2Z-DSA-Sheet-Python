#https://www.codingninjas.com/studio/problems/search-in-rotated-sorted-array_1082554?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def search(arr, n, k):
    left, right = 0, n - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == k:
            return mid
        
        if arr[left] <= arr[mid]:
            if arr[left] <= k < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[mid] < k <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1