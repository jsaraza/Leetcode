class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sumVal = 0
        start = 0
        minLength = len(nums) + 1

        for end in range(len(nums)):
            sumVal += nums[end]

            while(sumVal >= target):
                minLength = min(end-start + 1, minLength)
                sumVal -= nums[start]
                start += 1
        
        if minLength == len(nums) + 1:
            return 0
        else:
            return minLength
