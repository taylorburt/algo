


nums = [1,
        2,
        3,
        4,
        5]

def toJoin(sep, arr):
    if len(arr) == 0:
        return ""
    return str(arr[0]) + sep + str(toJoin(sep, arr[1:]))

def fizzBuzz(num):
    if num == 0:
        return
    result = num
    if num % 15 == 0:
        result = "FizzBuzz"
    elif num % 3 == 0:
        result = "Fizz"
    elif num % 5 == 0:
        result = "Buzz"
    return str(result) + "\n" + str(fizzBuzz(num - 1))
    

x = toJoin(" ", nums)
print(x)
print(fizzBuzz(101))

