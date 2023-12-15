#https://www.codingninjas.com/studio/problems/subarrays-with-sum-%E2%80%98k'_6922076?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def subarraysWithSumK( a:[int], k:int) ->[[int]]:
    result = []
    start = 0
    window_sum = 0
    current = []

    for end in range(len(a)):
        window_sum += a[end]
        current.append(a[end])

        while window_sum > k:
            window_sum -= a[start]
            current.pop(0)
            start += 1

        if window_sum == k:
            result.append(current[:])

    return result