def sum_digits(number):
    digit_sum = 0
    while number > 0:
        digit_sum += number % 10
        number //= 10
    return digit_sum
number = 345
result = sum_digits(number)
print(result)