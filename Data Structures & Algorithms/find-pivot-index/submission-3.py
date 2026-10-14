class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum, suffix_sum = [0] *n, [0]*n
        prefix_sum[0] = 0
        suffix_sum[-1] = 0

        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i-1] + nums[i-1]
        for i in range(n-2, -1, -1):
            suffix_sum[i] = suffix_sum[i+1] + nums[i+1]

        for i in range(n):
            if prefix_sum[i] == suffix_sum[i]:
                return i
        return -1