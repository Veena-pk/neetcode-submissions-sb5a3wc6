from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        res = []
        for num in nums:
            count[num] += 1
        sorted_count = sorted(count.items(), key = lambda x: x[1], reverse = True)
        for i in range(k):
            res.append(sorted_count[i][0])
        return res