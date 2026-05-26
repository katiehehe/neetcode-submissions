class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ptr1 = 0
        ptr2 = len(heights) - 1
        max_area = 0
        while ptr1 < ptr2:
            max_area = max(max_area, min(heights[ptr1], heights[ptr2]) * (ptr2 - ptr1))
            if heights[ptr1] < heights[ptr2]:
                ptr1 += 1
            elif heights[ptr2] < heights[ptr1]:
                ptr2 -= 1
            else:
                ptr1 += 1
                ptr2 -= 1
        return max_area