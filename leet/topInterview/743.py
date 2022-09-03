class Solution:
    def fizzBuzz(self, n: int):
        answer = []
        for i in range(1,n+1):
            if i%15==0:
                answer.append("FizzBuzz")
            elif i%3==0:
                answer.append("Fizz")
            elif i%5==0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return answer

s = Solution()
print(s.fizzBuzz(3))
print(s.fizzBuzz(5))
print(s.fizzBuzz(15))