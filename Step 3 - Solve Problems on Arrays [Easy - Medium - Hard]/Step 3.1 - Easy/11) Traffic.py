#https://www.codingninjas.com/studio/problems/traffic_6682625?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def traffic(n: int, m: int, vehicle: [int]) -> int:
    left = right = max_ones = zero_count = 0

    while right < n:
        if vehicle[right] == 0:
            zero_count += 1

        while zero_count > m:
            if vehicle[left] == 0:
                zero_count -= 1
            left += 1

        max_ones = max(max_ones, right - left + 1)
        right += 1

    return max_ones
