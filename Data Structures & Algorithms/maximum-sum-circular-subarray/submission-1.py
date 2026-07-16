class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        '''
        curr_max = 5-> max(5-3, -3) =2 -> max(2+5, 5) = 7
        global_max = 5 ->              -> max(5, 7) = 7
        
        [5,-3,5] total = 7

        curr_min = 5 -> min(5-3, -3) = -3 -> min(5-3, -3) = -3
        global_min = 5 -> min(5, -3) = -3 -> min(-3, -3) = -3

        total - global_min = 7 - (-3) = 10

        return max(global_max, total-global_min) = max(7, 10) = 10
        '''

        curr_max, curr_min = 0, 0
        global_max, global_min = nums[0], nums[0]
        total = 0

        for num in nums:
            total += num
            curr_max = max(curr_max + num, num)
            curr_min = min(curr_min + num, num)
            global_max = max(curr_max, global_max)
            global_min = min(curr_min, global_min)
        
        return max(global_max, total - global_min) if global_max > 0 else global_max

