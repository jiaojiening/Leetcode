class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        num_U = moves.count('U')
        num_D = moves.count('D')
        num_L = moves.count('L')
        num_R = moves.count('R')
        circle = False
        if (num_U==num_D) and (num_L==num_R):
            circle = True
        return circle
