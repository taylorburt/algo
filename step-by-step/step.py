
tot = 0
startValue = 0
min_value = 0
nums = [-3,2,-3,4,2]
for num in nums:
    tot = tot + num
    if tot < min_value:
        min_value = tot
print(tot)
print(-min_value + 1)
