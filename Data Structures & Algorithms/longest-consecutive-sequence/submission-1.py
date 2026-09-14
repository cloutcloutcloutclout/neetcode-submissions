class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        tset = set()
        for i in range(1,len(nums)):
            for j in range(len(nums)):
                if nums[j] + 1 == nums[i] and nums[j] != nums[i]:
                    count+=1
                    tset.add(j)
        return len(tset)
         