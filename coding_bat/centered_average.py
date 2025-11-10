def centered_average(nums):
    min_val = min(nums)
    max_val = max(nums)

    nums.remove(min_val)
    nums.remove(max_val)

    sum = 0
    deno = len(nums)

    for i in nums:
        sum = sum + i
        
    return sum // deno




print(centered_average([1, 2, 3, 4, 100])) # 3
print(centered_average([1, 1, 5, 5, 10, 8, 7])) # 5
print(centered_average([-10, -4, -2, -4, -2, 0])) # -3