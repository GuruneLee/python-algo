from copy import copy
class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(mat)
        for i in range(n//2):
            mat[i], mat[n-1-i] = mat[n-1-i], mat[i]
        for i in range(n):
            for j in range(i):
                mat[i][j], mat[j][i] =  mat[j][i],mat[i][j] 
                
    def rotate2(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        t = [mat[i].copy() for i in range(len(mat))]
        for i in range(len(mat)):
            mat[i] = [
                t[len(mat)-j-1][i] for j in range(len(mat))
            ]