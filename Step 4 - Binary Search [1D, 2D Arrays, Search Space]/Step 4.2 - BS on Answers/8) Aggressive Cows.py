#https://www.codingninjas.com/studio/problems/aggressive-cows_1082559?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def check_min_pos(stalls, min_dist, k):
    total_cows_placed = 1
    last_placed_cow = stalls[0]

    for i in range(1, len(stalls)):
        if stalls[i] >= last_placed_cow + min_dist:
            total_cows_placed += 1
            last_placed_cow = stalls[i]

    return total_cows_placed >= k
def aggressiveCows(stalls, k):
    stalls.sort()

    lower = 1
    higher = stalls[-1]
    ans = -1

    while lower <= higher:
        mid = lower + (higher - lower) // 2

        if check_min_pos(stalls, mid, k):
            ans = mid
            lower = mid + 1
        else:
            higher = mid - 1

    return ans
