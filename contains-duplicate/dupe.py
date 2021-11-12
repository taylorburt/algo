


def solve(nums):
    print(nums)
    # brute force
    # current = nums[0]
    # del nums[0]
    # while nums:
    #     for num in nums:
    #         if num == current:
    #             return True
    #     current = nums[0]
    #     del nums[0]

    # return False
    hashSet = set()
    for num in nums:
        if num in hashSet:
            return True
        hashSet.add(num)
    return False




print(solve([1,2,3,3]))