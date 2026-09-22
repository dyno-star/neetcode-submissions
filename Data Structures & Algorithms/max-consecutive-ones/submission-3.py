class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #iterate through array
        #initialize a variable to count number of times 1 is seen
        #compare, if that is the max return 
        current_count = 0
        max_count = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 1:
                current_count += 1

            else:
                current_count = 0
            if current_count > max_count:
                max_count = current_count
        return max_count 
