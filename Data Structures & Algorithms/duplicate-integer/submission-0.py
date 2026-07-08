class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)

        for num in nums:
            if counter[num] > 1:
                return True
        
        return False