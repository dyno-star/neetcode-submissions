class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = nums
        for i in range(n):
            arr.append(nums[i])
        return arr

        