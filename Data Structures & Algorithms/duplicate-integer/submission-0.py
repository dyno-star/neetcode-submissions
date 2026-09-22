class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        if sum(nums) - sum(set(nums)) == 0 and n == len(set(nums)):
            return False
        else:
            return True
         