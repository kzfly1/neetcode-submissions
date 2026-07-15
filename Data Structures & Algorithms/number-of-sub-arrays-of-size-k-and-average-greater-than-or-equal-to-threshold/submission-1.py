class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        count = 0

        for r in range(k - 1, len(arr)):
            sum_ = 0
            for i in range(l, r + 1):
                sum_ += arr[i]
            if sum_/k >= threshold:
                count += 1
            l += 1
        
        return count