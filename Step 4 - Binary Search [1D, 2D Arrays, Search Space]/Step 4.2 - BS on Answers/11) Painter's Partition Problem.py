#https://www.codingninjas.com/studio/problems/painter-s-partition-problem_1089557?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def partition_into_k(boards, max_paintable_area):
    total_painters = 1
    curr_area = 0

    for board in boards:
        curr_area += board
        if curr_area > max_paintable_area:
            total_painters += 1
            curr_area = board

    return total_painters
def findLargestMinDistance(boards:list, k:int):
    lower = max(boards)
    higher = sum(boards)

    while lower <= higher:
        mid = lower + (higher - lower) // 2

        if partition_into_k(boards, mid) > k:
            lower = mid + 1
        else:
            higher = mid - 1

    return lower