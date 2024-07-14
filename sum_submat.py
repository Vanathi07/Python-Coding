def maxMatrixSum(matrix):
    maxSum = -9999999
    n = len(matrix)
    m = len(matrix[0])
    top, left, right, bottom = None, None, None, None
    for i in range(n):
        for j in range(m):
            for k in range(n):
                for l in range(m):
                    currSum = 0
                    for x in range(i, k + 1):
                        for y in range(j, l + 1):
                            currSum += matrix[x][y]
                    if currSum > maxSum:
                        maxSum = currSum
                        top = i
                        left = j
                        right = k
                        bottom = l
print("The Top Left of the Rectangle is: ", top, left)
print("The Bottom Right of the Rectangle is: ", bottom, right)
print("The maximum sum is: ", maxSum)
