#https://www.codingninjas.com/studio/problems/generate-all-parenthesis_920445?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def validParenthesis(n: int) -> int:
    def generateParenthesisHelper(curr_str, open_count, close_count):
        if len(curr_str) == 2 * n:
            result.append(curr_str)
            return

        if open_count < n:
            generateParenthesisHelper(curr_str + '(', open_count + 1, close_count)

        if close_count < open_count:
            generateParenthesisHelper(curr_str + ')', open_count, close_count + 1)

    result = []
    generateParenthesisHelper('', 0, 0)
    return result