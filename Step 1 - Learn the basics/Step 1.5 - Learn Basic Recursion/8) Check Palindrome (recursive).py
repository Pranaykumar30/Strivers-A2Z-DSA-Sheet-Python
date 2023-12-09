#https://www.codingninjas.com/studio/problems/check-palindrome-recursive_624386?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def isPalindrome(string: str) -> bool:
    clean_string = ''.join(filter(str.isalnum, string.lower()))
    return clean_string == clean_string[::-1]
