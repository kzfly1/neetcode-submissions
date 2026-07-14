class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        [1,7,2,5,4,7,3,6]
        l              r
        area: 
        if heights[l] < heights[r]:
            area = (r-l) * heights[l]
            l += 1
        else:
            area = (r-l) * heights[r]
            r -= 1
        '''
        left = 0
        right = len(heights) - 1
        max_area = float("-inf")
        

        while left < right:
            if heights[left] < heights[right]:
                curr_area = (right - left) * heights[left]
                left += 1
            else:
                curr_area = (right - left) * heights[right]
                right -= 1
            
            max_area = max(max_area, curr_area)
        
        return max_area
