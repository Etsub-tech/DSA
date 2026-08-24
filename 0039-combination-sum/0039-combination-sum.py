class Solution(object):
    def combinationSum(self, candidates, target):
        result = []
        
        def dfs(start, path, remaining):
            if remaining == 0:
                result.append(path[:])  # found a valid combo
                return
            if remaining < 0:
                return  # too big, stop
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                dfs(i, path, remaining - candidates[i])  # reuse allowed
                path.pop()  # backtrack
        
        dfs(0, [], target)
        return result
