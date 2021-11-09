# Coin Change Problem

If I give you coins of denominations {3, 7, 9} (a coin worth 3 cents, a coin worth 7 cents, etc.), can you tell me the minimum number of coins that are needed to make a total of 37? You can assume that an infinite supply of all these coins are available to you.



This challenge is about solving the change making problem using dynamic programming. The task is to find the minimum number of coins that add up to a given denomination amount. We are given a set (via an array) of coins of different denominations and assume that each one of them has an infinite supply.

Examples
Here are a few examples of the given inputs and the expected output. Note, for all these examples other combinations are also possible. We are only interested in the minimum number of coins, regardless of the combination of coins.

SNIPPET
1. coins = {2,3,5}      amount = 11:     use 3 coins, e.g., [3,3,5]
2. coins = {2,3,5,7}    amount = 17:     use 3 coins, e.g., [3,7,7]
3. coins = {2,3,7}      amount = 15:     use 4 coins, e.g., [2,3,3,7]
4. coins = {3,5}        amount = 7:      Not possible (inf)
5. coins = {2,3,5}      amount = 1:      Not possible (inf)
For the combinations that are not possible, it is a convention to use infinity to represent such a solution.

Constraints
Length of array coins <= 1000
Each denomination will be a non zero positive integer
Amount will be a non zero value and <= 1000
Expected time complexity : O(n^2)
Expected space complexity : O(n)