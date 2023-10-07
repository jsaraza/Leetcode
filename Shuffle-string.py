class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        resultList = [None] * len(s)
        result = ""
        j = 0
        for i in indices:
            resultList[i] = s[j]
            j += 1
        
        for string in resultList:
            result += string

        return result