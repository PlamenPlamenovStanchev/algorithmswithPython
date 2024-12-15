def binary_search(nums, target):
    left_index = 0
    right_index = len(nums) - 1
    while left_index <= right_index:
        mid_idx = (left_index + right_index) // 2
        mid_el = nums[mid_idx]
        if mid_el == target:
            return mid_idx
        if target > mid_el:
            left_index = mid_idx + 1
        else:
            right_index = mid_idx - 1
    return - 1


nums = [int(x) for x in input().split()]
target = int(input())
print(binary_search(nums, target))
