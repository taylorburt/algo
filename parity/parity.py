def parity(nums):
    # For speed
    print(nums)
    odds = []
    evens = []
    result = []
    for i in nums:
        if i % 2:
            evens.append(i)
        else:
            odds.append(i)
    for i in range(len(nums)):
        if (i+1) % 2:
            result.append(evens[0])
            evens = evens[1:]
        else:
            result.append(odds[0])
            odds = odds[1:]
        print(result)
    return result

    # For memory





print(parity([4,2,5,7]))