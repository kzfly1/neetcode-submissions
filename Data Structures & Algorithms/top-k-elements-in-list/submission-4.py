class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        1. Build a frequency map that counts how many times each number appears
        2. Create a list of groups freq, where freq[i] will store all numbers that appear exactly i times
        3. For each number and its frequency in the map, add the number to freq[frequency]
        4. initialize an empty result list
        5. loop from the largest possible frequency down to 1:
           - for each number in the freq[i], add it to the result list
           - once the result contains k numbers, return it
        
        '''
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res




