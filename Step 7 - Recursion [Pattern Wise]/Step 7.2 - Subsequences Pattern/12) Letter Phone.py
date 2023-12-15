#https://www.codingninjas.com/studio/problems/letter-phone_626178?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf


from typing import List

def generateCombinations(digits: str, index: int, combination: str, mapping: List[str], result: List[str]):
    # Base case: If we have processed all digits, add the current combination to the result.
    if index == len(digits):
        result.append(combination)
        return

    # Get the letters corresponding to the current digit.
    letters = mapping[int(digits[index])]

    # Iterate over the letters and generate combinations.
    for letter in letters:
        combination += letter
        generateCombinations(digits, index + 1, combination, mapping, result)
        combination = combination[:-1]

def letterCombinations(digits: str) -> List[str]:
    # Mapping of digits to letters.
    mapping = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    # Result list to store the generated combinations.
    result = []
    combination = ""

    # Call the recursive function to generate combinations.
    generateCombinations(digits, 0, combination, mapping, result)

    # Return the result list containing the generated combinations.
    return result
