class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        seen_set = set([])
        while n != 1:
            if n in seen_set:
                return False
            else:
                digits = list()
                seen_set.add(n)
                while n:
                    digits.append(n % 10)
                    n //= 10
                
                n = sum([d ** 2 for d in digits])
        return True   
            