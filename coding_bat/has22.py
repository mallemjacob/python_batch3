def has22(nums):
    booly = False
    i = 0
    while i < len(nums) - 1:
        if nums[i] == 2 and nums[i + 1] == 2:
            booly = not booly
            break
        else:
            i = i + 1
    return booly

print(has22([1, 2, 2])) # True
print(has22([1, 2, 1, 2])) # False
print(has22([2, 1, 2])) # False