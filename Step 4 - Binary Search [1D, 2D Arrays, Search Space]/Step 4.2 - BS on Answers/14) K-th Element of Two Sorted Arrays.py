#https://www.codingninjas.com/studio/problems/k-th-element-of-2-sorted-array_1164159?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def kthElement(arr1: [int], n: int, arr2: [int], m: int, k: int) -> int:
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