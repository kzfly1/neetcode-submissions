class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        do it in place
        input: nums = [0, 1, 2, 2, 3, 0, 4, 2], 2
        ouput: 5; nums = [0,1,4,0,3, _, _, _]  2s were removed

        '''
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k 
