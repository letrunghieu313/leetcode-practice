# link: https://leetcode.com/problems/fizz-buzz/

def fizzBuzz(n):
    """
    :type n: int
    :rtype: List[str]
    """
    answer = []
    for i in range(1, n + 1):
        if (i % 3 == 0) and (i % 5 == 0):
            answer.append("FizzBuzz")
        elif(i % 3 == 0):
            answer.append("Fizz")
        elif(i % 5 == 0):
            answer.append("Buzz")
        else:
            answer.append(str(i))
    return answer


# We kinda messing up with initializing with the first iteration,
# we basically just need to use that straight i and go from there
# time complexity (n)
# space complexity (1)


print(fizzBuzz(n = 3))

