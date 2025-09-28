def min_removal(nums: list[int], k: int) -> int:
    nums.sort()
    if nums[0] * k <= nums[-1]:
        return 0
    # 1 2 6 9, 3
    #  1 4 3
    # two pointer?


