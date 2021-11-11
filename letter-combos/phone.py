
phoneHash = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}

digits = "23"

for digit in digits:
    print(digit)
    print(phoneHash[digit])

res = []
def backtrack(i, currentString):
    if len(currentString) == len(digits):
        res.append(currentString)
        return
    for c in phoneHash[digits[i]]:
        backtrack(i + 1, currentString + c)

if digits:
    backtrack(0, "")

print(res)
