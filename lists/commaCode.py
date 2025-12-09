spam = ['apples', 'bananas', 'tofu', 'cats', 'pigs']

# 'apples, bananas, tofu, and cats'

final_str = ''
for i in range(len(spam)): #4 range(4) = 0,1,2,3
    if i == len(spam) - 1: # 3 == 3
        final_str = final_str + 'and ' + spam[i]
    else:
        final_str = final_str + spam[i] + ', '
            
print(final_str)