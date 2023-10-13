class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = 0
        avg = -1000000
        start = 0

        for end in range(len(nums)):
            if end-start + 1 < k:
                currSum += nums[end]
            else:
                currSum += nums[end]
                avg = max(avg, currSum/k)
                currSum-= nums[start]
                start += 1
        
        return avg