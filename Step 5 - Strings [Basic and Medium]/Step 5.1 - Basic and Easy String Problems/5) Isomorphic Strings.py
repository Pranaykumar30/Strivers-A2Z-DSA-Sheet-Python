#https://www.codingninjas.com/studio/problems/isomorphic-strings-_1117636?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def areIsomorphic(str1: str, str2: str) -> bool:
    # Write your code here
    if len(str1) != len(str2):
        return False

    mapping = {}
    mapped = set()

    for i in range(len(str1)):
        if str1[i] in mapping:
            if mapping[str1[i]] != str2[i]:
                return False
        else:
            if str2[i] in mapped:
                return False
            mapping[str1[i]] = str2[i]
            mapped.add(str2[i])

    return True