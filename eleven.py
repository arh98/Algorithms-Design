
def max_water(heights_arr, n):

    left_max = n * [-1]
    right_max = n * [-1]

    left_max[0] = heights_arr[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], heights_arr[i])

    right_max[n-1] = heights_arr[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], heights_arr[i])

    waters = 0
    for i in range(n):
        min_height = min(left_max[i], right_max[i])
        if min_height > heights_arr[i]:
            waters += min_height - heights_arr[i]
    return waters


n = int(input())
heights = list(map(int, input().split()))
print(max_water(heights , n))
