class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter
        counts = Counter(nums)
        for value, count in counts.items():
            if count == 1:
                return value