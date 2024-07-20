class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m=len(rowSum)
        n=len(colSum)
        mat= [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                mat[i][j]=min(rowSum[i],colSum[j])
                rowSum[i]-=mat[i][j]
                colSum[j]-=mat[i][j]


        return mat
        