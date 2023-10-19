class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliments = {}

        for i in range(len(nums)):
            compliment = target - nums[i]

            if nums[i] in compliments:
                return [compliments[nums[i]], i]
            else:
                compliments[compliment] = i
        
        return []
