



def has_valid_subarray(nums: list[int], k: int):
    left = 0
    current_sum = 0
    found = 0
    d = [0]
    d.extend(nums)
    nums = d
    for right in range(1, len(nums)):
        current_sum += nums[right]
        while current_sum > k and left < right:
            current_sum -= nums[left]
            left += 1
        if current_sum == k:
            found += 1
    return found