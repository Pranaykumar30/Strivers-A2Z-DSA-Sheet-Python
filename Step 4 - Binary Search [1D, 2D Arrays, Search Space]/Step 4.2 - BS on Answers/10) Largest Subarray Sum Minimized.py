#https://www.codingninjas.com/studio/problems/largest-subarray-sum-minimized_7461751?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def no_of_subarray_possible(a, max_subarray_size):
    total_subarray_possible = 1
    curr_val = 0

    for num in a:
        curr_val += num
        if curr_val > max_subarray_size:
            total_subarray_possible += 1
            curr_val = num
    
    return total_subarray_possible
def largestSubarraySumMinimized(a: [int], k: int) -> int:
    lower = max(a)
    higher = sum(a)

    while lower <= higher:
        mid = lower + (higher - lower) // 2

        if no_of_subarray_possible(a, mid) > k:
            lower = mid + 1
        else:
            higher = mid - 1
    
    return lower