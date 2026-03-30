class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index_dict = {} # value -- > index
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in index_dict:
                return [index_dict[complement]+1, i+1]
            index_dict[num] = i