#https://www.codingninjas.com/studio/problems/majority-element_6783241?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def majorityElement(v: [int]) -> int:
    candidate = None
    count = 0

    for num in v:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    return candidate
