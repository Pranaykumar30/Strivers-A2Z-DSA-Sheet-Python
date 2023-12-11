#https://www.codingninjas.com/studio/problems/allocate-books_1090540?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def check_allocation(arr, mid, m):
    students = 1
    allocated_pages = 0

    for pages in arr:
        allocated_pages += pages
        if allocated_pages > mid:
            students += 1
            allocated_pages = pages

    return students <= m
def findPages(arr: [int], n: int, m: int) -> int:
    if n < m:
        return -1

    lower = max(arr)
    higher = sum(arr)
    result = -1

    while lower <= higher:
        mid = lower + (higher - lower) // 2

        if check_allocation(arr, mid, m):
            result = mid
            higher = mid - 1
        else:
            lower = mid + 1

    return result
    