#https://www.codingninjas.com/studio/problems/reverse-words-in-a-string_696444?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def reverseString(s: str) -> str:
    s_length = len(s) - 1
    ans = ""
    while s_length >= 0:
        while s_length >= 0 and s[s_length] == ' ':
            s_length -= 1

        word = ""
        while s_length >= 0 and s[s_length] != ' ':
            word += s[s_length]
            s_length -= 1

        ans += word[::-1]

        if s_length >= 0:
            ans += ' '

    return ans