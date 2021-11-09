

def maxArea(height) -> int:
    print(height)
    theMax = len(height)
    print(theMax)
    result = 0
    left = 0
    right = len(height) - 1
    while left < right:
        area = (right - left) * min(height[left], height[right])
        print("left: %s right: %s" % (height[left], height[right]))
        if area > result:
            result = area
        else:
            if height[left] > height[right]:
                right = right - 1
            elif height[right] > height[left] :
                left = left + 1
            elif height[left]  == height[right]:
                left = left +1
    return result


print(maxArea([2,3,4,5,18,17,6]))