class Solution(object):
    divisors = {1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"}

    def largestDivisor(self, n):
        divs = sorted(self.divisors.keys(), reverse=True)
        for d in divs:
            if n // d > 0:
                return d


    def intToRoman(self, n):
        """
        :type num: int
        :rtype: str
        """
        result = ""
        while n != 0:
            div = self.largestDivisor(n)
            rem = n - div
            result = result + self.divisors[div]
            n = rem
        return result