class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        difference = (nums[-1] * nums[-2]) - (nums[0] * nums[1])
        return difference