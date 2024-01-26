class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i, len(matrix[i])):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
                # print(matrix)

        for i in range(len(matrix)):
            for j in range(len(matrix[i]) // 2):
                temp = matrix[i][j]
                length = len(matrix[i])
                matrix[i][j] = matrix[i][length - j - 1]
                matrix[i][length - j - 1] = temp
        return matrix


  
