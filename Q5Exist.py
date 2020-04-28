class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        row = len(board)
        col = len(board[0])

        visited = [[0 for i in range(col)] for j in range(row)]

        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0] and (self.checkWord(board, word, i, j, 0, visited)):
                    return True
                else:
                    continue
        return False

    def checkWord(self, board, word, i, j, index, visited):

        if index == len(word):
            return True

        if (i < 0 or i >= len(board) or j < 0 or j >= len(board[i]) or board[i][j] != word[index]):
            return False

        if (visited[i][j]):
            return False

        visited[i][j] = True
        if (self.checkWord(board, word, i - 1, j, index + 1, visited) or
                self.checkWord(board, word, i + 1, j, index + 1, visited) or
                self.checkWord(board, word, i, j - 1, index + 1, visited) or
                self.checkWord(board, word, i, j + 1, index + 1, visited)):
            return True
        visited[i][j] = False

        return False
