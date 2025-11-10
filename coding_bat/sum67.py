
# find 6
# start another loop from 6, 
# skip numbers until 7, including it 

# Algorithmic thinking
# Problem Solving


def sum67(nums):
  
  
#   for i in range(len(nums)):
#     if nums[i] == 6:
#       for j in range(i,len(nums)):
#         if nums[j] == 7:
#           continue
#     else:
#       sum = sum + nums[i]

#     return sum  
    
    
    sum = 0
    i = 0
    while i < len(nums): # 0 < 9
        if nums[i] == 6:
            for j in range(i+1,len(nums)): #6, 10
                if nums[j] == 7:
                    i = j + 1
                    break
                else:                    
                    i = j + 1
        else:
            sum = sum + nums[i]
            i = i + 1
    return sum
        
print(sum67([1, 2, 2])) #5
print(sum67([1, 2, 2, 6, 99, 99, 7, 4, 2])) # 11
print(sum67([1, 1, 6, 7, 2])) #4

# spam = [1, 2, 2, 6, 99, 99, 7, 4, 2]

# sum1 = 0
# sum2 = 0

# index1 = spam.index(6)
# print(index1)

# index2 = spam.index(7)
# print(index2)

# for i in range(0, index1):
#     sum1 = sum1 + spam[i]

# for i in range(index2 + 1, len(spam)):
#     sum2 = sum2 + spam[i]

# print(sum1 + sum2)



# if nums.index(6):
#         index1 = nums.index(6)
#         sum1 = sum1 + nums[i]

# def sum67(nums):
#     sums = 0
#     add = True

#     for i in nums:
#         if i == 6:
#             add = False
#         elif i == 7 and not add:
#             add = True
#         elif add:
#             sums = sums + i
#     return sums

        
# print(sum67([1, 2, 2])) #5
# print(sum67([1, 2, 2, 6, 99, 99, 7, 4, 2])) # 11
# print(sum67([1, 1, 6, 7, 2])) #4
