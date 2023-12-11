#https://www.codingninjas.com/studio/problems/minimise-max-distance_7541449?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def check_distance(arr, k, min_dist):
    total_added_gas_stations = 0

    for i in range(1, len(arr)):
        total_added_gas_stations += ((arr[i] - arr[i - 1]) / min_dist) - 1

    return total_added_gas_stations <= k
def minimiseMaxDistance(arr: [int], k: int) -> float:
    left = 0.0
    right = float(arr[-1])

    while right - left > 1e-6:
        mid = left + (right - left) / 2

        if check_distance(arr, k, mid):
            right = mid
        else:
            left = mid

    return right