class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        length = len(nums)

        '''
        for i in range(1,len(nums)):
            if nums[i] == nums[j]:
                return True
            else:
                j+=1
        return False
        '''

        for i in range(length - 1):
            for j in range(i + 1, length):
                if nums[i] == nums[j]:
                    return True
        return False
                


