class Solution:
    def isPalindrom(self, n: str) -> str:
        if n == n[::-1]:
            return True
        else:
            return False
        
    def mirrorString(self, n: str) -> str:
        """
        EMirror a string to form a palindrome.
        For even length: mirror the first half.
        For odd length: mirror the first half + middle digit, then mirror the first half.
        xample: "abcde" -> "abcba".
        """
        # n[start:end:step] slicing returns characters from indexes 'start' to 'end'-1,
        # stepping by 'step' (negative is reverses).
        mid = len(n) // 2 
        leftSide = n[0:mid:]                 # "abcde" --> "ab"
        leftSideRevresed = leftSide[::-1]    # "ab" --> "ba"

        # handle even and odd length strings.
        # For even length: "abcd" -> "ab" + "ba" = "abba".
        # For odd length: "abcde" -> "ab" + "c" + "ba" = "abcba".
        if len(n) % 2 == 0: # even length
            mirror_L2R = leftSide + leftSideRevresed
        else: # odd length
            mirror_L2R = leftSide + n[mid] + leftSideRevresed

        return mirror_L2R

    def nearestPalindromic(self, n: str) -> str:
        num = int(n)
        length = len(n)

        # Handle edge cases
        # case of single char: 1,2,3,4,5,6,7,8,9
        if num >= 1 and num <= 9: 
            # if the number is between 1 to 10, return the previous number
            return str(num-1)
        # case of: 10,100,1000, ...
        elif num == 10 ** (length-1):
            return str(num-1) # 9, 99, 999, ...
        # # case of: 11, 101, 1001, ...
        # elif num == 10 ** (length-1) + 1:
        #     return str(num-2) # 9, 99, 999, ...

        # case of: 99,999, ...
        elif num == 10**length - 1:
            return str(num + 2) # 101, 1001, 10001, ...
        
        # --- general case ---
        
        # mirror the string to form a palindrome
        mirror = int(self.mirrorString(n)) 

        # find the next palindrome by adding or subtracting the changeScale.
        # scale is detemined by the length of the string, 
        # because odd length has a middle digit, even length does not.
        mid = len(n) // 2 
        lenghtIsEven = len(n) % 2 == 0

        if lenghtIsEven: 
            scale = 11 * 10**(mid-1) # = 1100..... with l/2 zeros
        else: 
            # odd
            scale = 10 ** (mid-1) # = 1000..... with l/2 zeros

        # determine scale's sign by whether we need to add or subtract the 
        rightSide = n[mid:] 
        if int(rightSide) >= scale/2:
            scale =  +scale # positive 
        else: 
            scale =  -scale # negative

        # Find next palindrome
        nextPalindrome = mirror
        while not self.isPalindrom(str(nextPalindrome)) or nextPalindrome <= 0:
            nextPalindrome += scale

        # check witch one is the closest result
        res = ""
        # Handle self-palindrome case
        if num == mirror:
            return str(nextPalindrome)
        
       # Return closest (or smaller if tie)
        diff1 = abs(num - mirror)
        diff2 =  abs(num - nextPalindrome)
        if diff1 < diff2:
            res = str(mirror)
        elif diff1 > diff2:
            res = str(nextPalindrome)
        else:
            # Tie, so take the smallest one
            res = str(min(mirror, nextPalindrome))
        
        return res


# if __name__ == "__main__":
#     n = "111"
#     finder = Solution()
#     result = finder.nearestPalindromic(n)
#     print(f"The closest palindrome to {n} is: {result}")
