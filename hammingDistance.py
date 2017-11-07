class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # mid_x = []
        # mid_y = []
        # while True:
            # if x == 0: break
            # num,rem = divmod(num, 2)
            # mid_x.append(base[rem])
        mid_x = bin(x).replace('0b','')
        mid_y = bin(y).replace('0b','')
        if len(mid_x) > len(mid_y):
            mid_y = (len(mid_x)-len(mid_y))*'0' + mid_y
        else:
            mid_x = (len(mid_y)-len(mid_x))*'0' + mid_x
        D = 0
        for i in range(0, len(mid_x)):
            D += (int(mid_x[i]) - int(mid_y[i]))**2
        return D
