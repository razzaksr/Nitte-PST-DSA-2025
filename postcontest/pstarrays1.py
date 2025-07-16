def rotate_image(matrix):
    size = len(matrix)
    # Transpose
    for row in range(size):
        for column in range(row, size):
            matrix[row][column], matrix[column][row] = matrix[column][row], matrix[row][column]
    # Reverse each row
    for row in range(size): matrix[row].reverse()
    return matrix

def rotate_image2(matrix):
    n = len(matrix)
    for i in range(n//2):
        for j in range(i,n-1-i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n-1-j][i]
            matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
            matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
            matrix[j][n-i-1]=temp
    return matrix


# Example usage:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
print("Rotate Image:", rotate_image([[1,2,3],[4,5,6],[7,8,9]]))
print("Rotate Image:", rotate_image2([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))    
        



            





