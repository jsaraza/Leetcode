class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        ptrTwo = 1

        for ptrOne in range(len(nums)):
            if nums[ptrOne] == 0:
                ptrTwo = ptrOne
                while(nums[ptrTwo] == 0):
                    ptrTwo += 1
                    if ptrTwo == len(nums):
                        return
                
                temp = nums[ptrOne]
                nums[ptrOne] = nums[ptrTwo]
                nums[ptrTwo] = temp