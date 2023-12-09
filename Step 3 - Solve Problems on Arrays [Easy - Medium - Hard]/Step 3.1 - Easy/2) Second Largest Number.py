#https://www.codingninjas.com/studio/problems/ninja-and-the-second-order-elements_6581960?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    if n < 2:
        return []

    max_element = max(a[0], a[1])
    second_max = min(a[0], a[1])

    min_element = min(a[0], a[1])
    second_min = max(a[0], a[1])

    for i in range(2, n):
        if a[i] > max_element:
            second_max = max_element
            max_element = a[i]
        elif a[i] > second_max and a[i] != max_element:
            second_max = a[i]

        if a[i] < min_element:
            second_min = min_element
            min_element = a[i]
        elif a[i] < second_min and a[i] != min_element:
            second_min = a[i]

    return [second_max, second_min]
