class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        j = 0 

        for i in range(1,len(nums)):
            if nums[i] != nums[j]:
                j+=1
            else:
                return True
        return False