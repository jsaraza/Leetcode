class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Hmap = {}

        for i in range(len(nums)):
            compliment = target - nums[i]

            if compliment in Hmap:
                return [Hmap[compliment], i]
            
            Hmap[nums[i]] = i
