#https://www.codingninjas.com/studio/problems/roman-numeral-to-integer_981308?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def romanToInt(s:str) -> int:
    mp = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ans = 0

    i = 0
    while i < len(s):
        if i != len(s) - 1 and mp[s[i + 1]] > mp[s[i]]:
            ans += mp[s[i + 1]] - mp[s[i]]
            i += 2
        else:
            ans += mp[s[i]]
            i += 1

    return ans