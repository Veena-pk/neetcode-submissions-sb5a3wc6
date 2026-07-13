class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_pdct = [1] * n
        suffix_pdct = [1] * n
        array_pdct = [1] * n
        for i in range(1, n):
            prefix_pdct[i] = nums[i-1] * prefix_pdct[i-1]
        for i in range(n-2, -1, -1):
            suffix_pdct[i] = nums[i+1] * suffix_pdct[i+1]
        for i in range(n):
            array_pdct[i] = prefix_pdct[i] * suffix_pdct[i]
        return array_pdct