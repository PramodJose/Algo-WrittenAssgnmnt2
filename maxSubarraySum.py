def mss(arr, low, high):
    if high == low:                     # if there is only one element in the array, then it itself is the
        return low, high, arr[high]     # largest element and the largest sum in that array.
    
    mid = (low + (high - low)//2)   # same as (low + high) // 2; but prevents overflows.

    leftlow, lefthigh, leftsum = mss(arr, low, mid)
    rightlow, righthigh, rightsum = mss(arr, mid + 1, high)
    xlow, xhigh, xsum = cross(arr, low, mid, high)

    if (leftsum > rightsum) and (leftsum > xsum):
        return leftlow, lefthigh, leftsum
    elif (rightsum > leftsum) and (rightsum > xsum):
        return rightlow, righthigh, rightsum
    else:
        return xlow, xhigh, xsum


def cross(arr, low, mid, high):
    sum = 0
    maxleft = mid
    leftsum = arr[maxleft]

    for i in range(mid, low - 1, -1):
        sum += arr[i]
        if sum > leftsum:
            leftsum = sum
            maxleft = i

    sum = 0
    maxright = mid + 1
    rightsum = arr[maxright]

    for i in range(mid + 1, high + 1):
        sum += arr[i]
        if sum > rightsum:
            rightsum = sum
            maxright = i

    return maxleft, maxright, leftsum + rightsum


arr = [1, -4, 3, 4, -2, 6]
# arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(mss(arr, 0, len(arr) - 1))
