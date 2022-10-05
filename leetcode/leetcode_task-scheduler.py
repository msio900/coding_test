class Solution:
    # def fib(self, n: int) -> int:
    #     if n <= 1:
    #         return n
    #     return self.fib(n - 1) + self.fib(n - 2)
    def fib(n: int) -> int:
        if n <= 1:
            return n
        return Solution.fib(n - 1) + Solution.fib(n - 2)

# sol = Solution()
# print(sol.fib(5))
#
# if __name__ == "__main__":
#     print(Solution().fib(n=5))
#
if __name__ == "__main__":
    print(Solution.fib(5))