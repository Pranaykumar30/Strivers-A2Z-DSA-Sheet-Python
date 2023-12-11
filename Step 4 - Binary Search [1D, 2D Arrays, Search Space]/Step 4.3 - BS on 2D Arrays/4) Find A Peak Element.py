#https://www.codingninjas.com/studio/problems/find-peak-element_7449073?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def findPeakGrid(g: [[int]]) -> [int]:
    rows = len(g)
    cols = len(g[0])

    lower = 0
    higher = rows - 1

    while lower <= higher:
        mid = lower + (higher - lower) // 2

        coln = -1
        maxi = -1

        for i in range(cols):
            if maxi < g[mid][i]:
                maxi = g[mid][i]
                coln = i
        
        if mid + 1 < rows and g[mid + 1][coln] >= g[mid][coln]:
            lower = mid + 1
        elif mid - 1 >= 0 and g[mid - 1][coln] >= g[mid][coln]:
            higher = mid - 1
        else:
            return [mid, coln]
    
    return [-1, -1]