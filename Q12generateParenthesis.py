class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.helper_generateParanthesis(n, n, res, "")
        return res

    def helper_generateParanthesis(self, Lpar, Rpar, res, parString):
        if (Lpar == 0 and Rpar == 0):
            res.append(parString)

        if (Lpar > 0):
            self.helper_generateParanthesis(Lpar - 1, Rpar, res, parString + "(")

        if (Lpar < Rpar):
            self.helper_generateParanthesis(Lpar, Rpar - 1, res, parString + ")")

        return parString