#https://www.codingninjas.com/studio/problems/minimum-rate-to-eat-bananas_7449064?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def minimumRateToEatBananas(v: [int], h: int) -> int:
    low, high = 1, max(v)

    while low < high:
        mid = low + (high - low) // 2
        total_hours = sum((pile + mid - 1) // mid for pile in v)

        if total_hours <= h:
            high = mid
        else:
            low = mid + 1

    return low