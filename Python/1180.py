__________________________________________________________________________________________________
class Solution:
    def countLetters(self, S: str) -> int:
        n = len(S)
        res = 1
        cur = 1
        for i in range(1, n):
            if S[i] == S[i - 1]: 
                cur += 1
            else:
                cur = 1
            res += cur
        return res
__________________________________________________________________________________________________

__________________________________________________________________________________________________
