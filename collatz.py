# 1. Write collatz() function
# 2. It takes a parameter: number (n)
# 3.if number is even ---> print and return (number // 2).
# 4.if number is odd --> print and return (3 * number + 1)
# 5.The function keeps running until it return 1

def collatz(n):
    if n % 2 == 0:
        print(n // 2)
        return n // 2
    else:
        print(3 * n + 1)
        return 3 * n + 1

while True:
    try:
        user_input = int(input('Enter a interger number: '))
        count = 0
        while True:
            count += 1
            return_value = collatz(user_input)
            if return_value == 1:
                break
            else:
                user_input = return_value

        print("number of times: " + str(count))
        break
    except ValueError:
        print('Must be interger!')
    except KeyboardInterrupt:
        print('The end!')
        break