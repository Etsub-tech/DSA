class Solution(object):
    def combine(self, n, k):
        res = []

        def backtrack(curr, start):
            if len(curr) == k:
                res.append(curr[:])  
                return

            for j in range(start, n + 1):
                curr.append(j)            
                backtrack(curr, j + 1)      
                curr.pop()                  

        backtrack([], 1)
        return res
