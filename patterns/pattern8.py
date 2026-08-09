class Solution:
    def pattern8(self, n):
        for i in range(n,0,-1):
            for j in range(n-i+1):
                print(" ", end="")
            for k in range(2*i-1):
                print("*", end="")  
            print()

if __name__ == "__main__":

    sol = Solution()
    sol.pattern8(5)