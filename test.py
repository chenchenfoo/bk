import sys
class Solution:
    """
    @param: heights: a vector of integers
    @return: an integer
    """
    '''
    def maxArea(self, heights):
        # write your code here
        start, end = 0, len(heights) - 1
        result = 0
        while start < end:
            tmp = min(heights[start], heights[end]) * (end - start)
            if tmp > result:
                result = tmp
            if heights[start] > heights[end]:
                end -= 1
            else:
                start += 1
        return result

    def trapRainWater(self, heights):
        # write your code here
        result = 0
        start, end = 0, len(heights) - 1
        maxS = maxE = 0
        while start < end:
            if heights[start] <= heights[end]:
                maxS = max(maxS, heights[start])
                result += maxS - heights[start]
                start += 1
            else:
                maxE = max(maxE, heights[end])
                result += maxE - heights[end]
                end -= 1
        return result
    '''

    def spiralOrder(self, matrix):
        # write your code here
        if matrix == []:
            return []
        start = top = 0
        end = len(matrix[0]) -1
        bottom = len(matrix) -1
        result = []
        while start < end and top < bottom:
            for i in range(start, end):
                result.append(matrix[top][i])
            for i in range(top, bottom):
                result.append(matrix[i][end])
            for i in range(end, start, -1):
                result.append(matrix[bottom][i])
            for i in range(bottom, top, -1):
                result.append(matrix[i][start])
            start += 1
            end -= 1
            top += 1
            bottom -= 1

        if start == end and top == bottom:
            result.append(matrix[top][start])
        elif start == end:
            for i in range(top, bottom + 1):
                result.append(matrix[i][start])
        elif top == bottom:
            for i in range(start, end + 1):
                result.append(matrix[top][i])
        return result

    def smallestDifference(self, A, B):
        # write your code here
        if not A or not B:
            return 0
        A.sort()
        B.sort()

        lenA = len(A)
        lenB = len(B)

        a, b = 0, 0
        tmp = 0
        result = 0

        while a < lenA - 1 and b < lenB - 1:
            result = abs(A[a] - B[b])
            if abs(A[a] - B[b]) < abs(A[a] - B[b+1]):
                a += 1
            else:
                b += 1
        return result

    def setZeroes(self, matrix):
        # write your code here
        m = len(matrix)
        n = len(matrix[0])
        row = [0 for i in range(m)]
        col = [0 for i in range(n)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = 1
                    col[j] = 1
        for i in range(m):
            for j in range(n):
                if row[i] == 1 or col[j] == 1:
                    matrix[i][j] = 0
        return matrix

    def find132pattern(self, nums):
        # Write your code here

        n = len(nums)
        if n <= 2:
            return False

        minPre = [0] * n
        minPre[0] = nums[0]
        for i in range(1, n):
            minPre[i] = min(minPre[i - 1], nums[i])
        print minPre

        maxStack = []
        for j in range(n - 1, 0, -1):
            max = -sys.maxint
            while len(maxStack) > 0 and maxStack[-1] < nums[j]:
                max = maxStack.pop()
            if minPre[j - 1] < max:
                return True
            maxStack.append(nums[j])
        return False



if __name__ == "__main__":
    #A = [3,6,7,4]
    #B = [2,8,9,3]
    #matrix = [[1, 2], [0, 3]]
    nums = [1, 2, 3, 4]

    #result1 = Solution().continuousSubarraySum(A)
    #result2 = Solution().setZeroes(matrix)
    result = Solution().find132pattern(nums)
    print result
