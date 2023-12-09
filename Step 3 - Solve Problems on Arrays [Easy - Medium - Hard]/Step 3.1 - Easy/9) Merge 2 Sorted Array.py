#https://www.codingninjas.com/studio/problems/sorted-array_6613259?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def sortedArray(a: [int], b: [int]) -> [int]:
     m = len(a)
     n = len(b)
     result = []
     i = 0  # Pointer for array a
     j = 0  # Pointer for array b

     while i < m and j < n:
        if a[i] < b[j]:
            if not result or a[i] != result[-1]:
                result.append(a[i])
            i += 1
        elif a[i] > b[j]:
            if not result or b[j] != result[-1]:
                result.append(b[j])
            j += 1
        else:
            if not result or a[i] != result[-1]:
                result.append(a[i])
            i += 1
            j += 1

    # Add remaining elements from a
     while i < m:
        if not result or a[i] != result[-1]:
            result.append(a[i])
        i += 1

    # Add remaining elements from b
     while j < n:
        if not result or b[j] != result[-1]:
            result.append(b[j])
        j += 1

     return result