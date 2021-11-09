class Solution:
    def twoSum(self, nums, target):
        for x in range(len(nums)):
            temp = 1 + x
            while True:
                try:
                    total = nums[x] + nums[temp]
                    if total == target:
                        print(x)
                        print(temp)
                        print(total)
                        return x-1, temp-1
                    else:
                        temp = temp + 1
                except:
                    break
                


sol = Solution()
val = sol.twoSum([3,2,4], 6)
print(val)