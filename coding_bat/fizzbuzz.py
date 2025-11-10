def fizzbuzz(n):
    output_list = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            output_list = output_list + ['fizzbuzz']
        elif i % 3 == 0:
            output_list = output_list + ['fizz']
        elif i % 5 == 0:
            output_list = output_list + ['buzz']
        else:
            output_list = output_list + [str(i)]
    return output_list    

print(fizzbuzz(50))