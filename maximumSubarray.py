def maxiumSub(nums):
    # Kadane's Algorithm
    max_current = max_global = nums[0]
    n = len(nums)
    for i in range(1, n):
        max_current = max(nums[i], max_current + nums[i])
        if max_current > max_global:
            max_global = max_current
    return max_global

    # output = 0
    # n = len(nums)
    # for i in range(n):
    #     for j in range(1, n):
    #         sum1 = 0
    #         for k in range(i, j):
    #             sum1 += nums[k]
    #             if (sum1 > output):
    #                 output = sum1
    # return output

    # maxSub = nums[0]
    # curSum = 0
    # for n in nums:
    #     if curSum < 0:
    #         curSum = 0
    #     curSum += n
    #     maxSub = max(maxSub, curSum)
    # return maxSub


lst = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxiumSub(lst))
