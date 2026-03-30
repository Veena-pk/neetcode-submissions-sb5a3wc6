class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_water = float('-inf')

        while l < r:
            total_water = (r - l) * min(heights[r], heights[l])
            max_water = max(max_water, total_water)

            if min(heights[r], heights[l]) == heights[l]:
                l += 1
            else:
                r -= 1

        return max_water