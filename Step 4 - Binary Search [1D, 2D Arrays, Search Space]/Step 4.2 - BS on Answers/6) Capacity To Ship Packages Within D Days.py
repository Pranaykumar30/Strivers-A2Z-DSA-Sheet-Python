#https://www.codingninjas.com/studio/problems/capacity-to-ship-packages-within-d-days_1229379?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from os import *
from sys import *
from collections import *
from math import *
def check_min_weight(weights, min_weight, d):
    total_days = 1
    weight_till_now = 0

    for weight in weights:
        weight_till_now += weight
        if weight_till_now > min_weight:
            total_days += 1
            weight_till_now = weight
        if total_days > d:
            return False
    return True
def leastWeightCapacity(weights, d):
    lower = max(weights)
    higher = sum(weights)
    ans = -1

    while lower <= higher:
        mid = lower + (higher - lower) // 2

        if check_min_weight(weights, mid, d):
            ans = mid
            higher = mid - 1
        else:
            lower = mid + 1

    return ans