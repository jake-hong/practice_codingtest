def two_sum(nums, target):
    memo = {}

    for v in nums:
        needed_number = target - v
        if needed_number in memo:
            return True
        memo[v] = True
    return False

two_sum(nums =[4,1,6,7,8,2], target=14)