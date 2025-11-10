def sum13(nums):
    sum = 0
    i = 0

    while i < len(nums): # 0 < 7
        if nums[i] == 13:
            i = i + 2
        else:
            sum = sum + nums[i]
            i = i + 1
    return sum


print(sum13([1, 2, 2, 1])) # 6
print(sum13([1, 1])) # 2
print(sum13([1, 2, 2, 1, 13])) # 6
print(sum13([1, 2, 2, 1, 13, 7, 2])) # 8


