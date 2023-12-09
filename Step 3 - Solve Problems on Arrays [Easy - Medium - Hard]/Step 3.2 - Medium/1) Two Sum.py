#https://www.codingninjas.com/studio/problems/reading_6845742?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def read(n: int, book: [int], target: int) -> str:
    pages = {}
    
    for num in book:
        if target - num in pages:
            return "YES"
        pages[num] = True
    
    return "NO"
