class Solution:
    def generateParenthesis(self, n):
        res = []

        def backtrack(s, open_count, close_count):
            # If the string is complete, add to results
            if len(s) == 2 * n:
                res.append(s)
                return
            # Add '(' if we still have some left
            if open_count < n:
                backtrack(s + "(", open_count + 1, close_count)
            # Add ')' only if it won’t break validity
            if close_count < open_count:
                backtrack(s + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return res
