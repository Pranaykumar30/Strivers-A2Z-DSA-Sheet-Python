#https://www.codingninjas.com/studio/problems/anagram-pairs_626517?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def isAnagram(str1, str2) :
	# Create dictionaries to count occurrences of characters
    count_str1 = {}
    count_str2 = {}

    # Count occurrences of characters in str1
    for char in str1:
        count_str1[char] = count_str1.get(char, 0) + 1

    # Count occurrences of characters in str2
    for char in str2:
        count_str2[char] = count_str2.get(char, 0) + 1

    # Check if both dictionaries are equal
    return count_str1 == count_str2