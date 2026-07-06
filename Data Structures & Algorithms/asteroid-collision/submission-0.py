class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                total = a + stack[-1]
                if total < 0:
                    stack.pop()
                elif total > 0:
                    a = 0
                    break
                else:
                    a = 0
                    stack.pop()
            if a != 0:
                stack.append(a)
        return stack