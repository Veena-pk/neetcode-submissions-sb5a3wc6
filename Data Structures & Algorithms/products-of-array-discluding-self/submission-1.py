class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_pdct = [1] * len(nums)
        suffix_pdct = [1] * len(nums)
        array_pdct = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix_pdct[i] = nums[i-1] * prefix_pdct[i-1]
        for i in range(len(nums)-2, -1, -1):
            suffix_pdct[i] = nums[i+1] * suffix_pdct[i+1]
        for i in range(len(nums)):
            array_pdct[i] = prefix_pdct[i] * suffix_pdct[i]
        return array_pdct