class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        # min_row_values = {min(row) for row in matrix}
        # max_col_values = {max(col) for col in zip(*matrix)}
        # return list(min_row_values & max_col_values)

        lucky_numbers = []
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            min_value = matrix[i][0]
            min_index = 0
            for j in range(1, cols):
                if matrix[i][j] < min_value:
                    min_value = matrix[i][j]
                    min_index = j
            

            is_lucky = True
            for k in range(rows):
                if matrix[k][min_index] > min_value:
                    is_lucky = False
                    break
            
            if is_lucky:
                lucky_numbers.append(min_value)
        
        return lucky_numbers