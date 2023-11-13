
def matrix_to_array(matrix):
    new_arr = []
    penalty = 0
    for i, row in enumerate(matrix):
        row_penalty = min(row)
        # penalty = min(row) if min(row) < penalty else 0
        if row_penalty<penalty:
            penalty = row_penalty

        if i % 2 == 0:
            new_arr += row + [penalty]
        else:
            new_arr += list(reversed(row)) + [penalty]
    return new_arr

def max_subarray(arr):
    if len(arr) == 1:
        return arr[0]
    
    mid = len(arr) // 2
    
    left_max = max_subarray(arr[:mid])
    right_max = max_subarray(arr[mid:])
    
    max_left_sum = float('-inf')
    left_sum = 0
    for i in range(mid - 1, -1, -1):
        left_sum += arr[i]
        max_left_sum = max(max_left_sum, left_sum)
    
    max_right_sum = float('-inf')
    right_sum = 0
    for i in range(mid, len(arr)):
        right_sum += arr[i]
        max_right_sum = max(max_right_sum, right_sum)
    
    return max(left_max, right_max, max_left_sum + max_right_sum)

m = int(input())
n = int(input())
matrix = []
for i in range(m):
    row = list(map(float, input().split()))
    matrix.append(row)

myArr = matrix_to_array(matrix)
# print(myArr)
# k = len(myArr) 
max_sum = max_subarray(myArr)
print("maxProfit=",int(max_sum)) 
