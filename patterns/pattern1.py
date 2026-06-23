class Solution:
    def pattern1(self, n):
        for i in range(n):
            for j in range(n):
                print ("*", end="")
            print()



if __name__ == "__main__":

    sol = Solution()
    sol.pattern1(6)