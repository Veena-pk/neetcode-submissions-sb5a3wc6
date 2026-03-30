class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        count_zero = 0
        zero_index = -1
        res = []
        for i in range(len(nums)):
            if nums[i] == 0:
                count_zero += 1
                zero_index = i
            else:
                product *= nums[i]
        
        if count_zero > 1:
            return [0] * len(nums)

        elif count_zero == 1:
            res = [0] * len(nums)
            res[zero_index] = product
            return res

        else:
            for i in range(len(nums)):
                res.append(product // nums[i])
            return res