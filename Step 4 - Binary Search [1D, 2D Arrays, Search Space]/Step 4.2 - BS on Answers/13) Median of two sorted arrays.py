#https://www.codingninjas.com/studio/problems/median-of-two-sorted-arrays_985294?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def kth_element(arr1, arr2, n, m, k):
    flower, fhigher = 0, n - 1
    slower, shigher = 0, m - 1

    while flower <= fhigher and slower <= shigher:
        fmid = flower + (fhigher - flower) // 2
        smid = slower + (shigher - slower) // 2

        number_covered_till_now = fmid + smid + 1

        if arr1[fmid] > arr2[smid]:
            if number_covered_till_now >= k:
                fhigher = fmid - 1
            else:
                slower = smid + 1
        else:
            if number_covered_till_now >= k:
                shigher = smid - 1
            else:
                flower = fmid + 1

    if flower > fhigher:
        return arr2[slower + (k - flower - slower) - 1]
    else:
        return arr1[flower + (k - flower - slower) - 1]
def median(a: int, b: int) -> float:
    total_size = len(a) + len(b)
    if total_size % 2 == 0:
        ans = kth_element(a, b, len(a), len(b), total_size // 2) + kth_element(a, b, len(a), len(b), total_size // 2 + 1)
        ans /= 2
        return ans
    else:
        return kth_element(a, b, len(a), len(b), total_size // 2 + 1)
