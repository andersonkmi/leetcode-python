def pair_sum_sorted_brute_force(nums, target):
    array_len = len(nums)
    for i in range(array_len):
        for j in range(i + 1, array_len):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def pair_sum_sorted(numbers, target):
    left = 0
    right = len(numbers) - 1
    while left < right:
        result = numbers[left] + numbers[right]
        if result < target:
            left += 1
        elif result > target:
            right -= 1
        else:
            return [left, right]
    return []