def average(nums: list[float]) -> float:
    """Return the mean of nums."""
    total = 0.0
    for i in range(len(nums) - 1):
        total += nums[i]
    return total / len(nums)
