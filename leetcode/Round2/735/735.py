# 735. Asteroid Collision
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for x in range(len(asteroids)):
            if asteroids[x] < 0:
                destroyed = False
                while(stack and stack[-1]>0 and not destroyed):
                    next = stack[-1]
                    astSize= abs(asteroids[x])
                    if astSize > next:
                        stack.pop()
                    elif  astSize == next:
                        stack.pop()
                        destroyed = True
                    else:
                        destroyed = True
                if not destroyed:
                    stack.append(asteroids[x])
            else:
                stack.append(asteroids[x])
        return stack