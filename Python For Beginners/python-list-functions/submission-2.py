from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    sum_res = 0
    for num in nums:
        sum_res += num
    
    return sum_res

def get_min(nums: List[int]) -> int:
    # use build-in (min())
    min_value = float("inf")
    for num in nums:
        min_value = min(num, min_value)
    return min_value

def get_max(nums: List[int]) -> int:
    # without built-in approach
    max_value = nums[0]
    for num in nums:
        if num > max_value:
            max_value = num
    return max_value

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
