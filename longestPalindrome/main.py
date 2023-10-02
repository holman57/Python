class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]: return s
        l = 0
        m = len(s) - 1
        w = m
        r = l + w - 1
        while w > 1:
            while r <= m:
                sub = s[l:r+1]
                rsub = sub[::-1]
                if sub == rsub: return sub
                l += 1
                r += 1
            w -= 1
            l = 0
            r = l + w - 1
        return s[0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestPalindrome("abb"))
