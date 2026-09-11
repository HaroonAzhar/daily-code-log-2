# 735. Asteroid Collision
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s=[]
            
        for a in asteroids:
            if a < 0:
                while s and s[-1]>0 and s[-1]<abs(a):
                    s.pop()
                    
                if not s or s[-1]<0:
                    s.append(a)
                else:
                    if s[-1]==abs(a):
                        s.pop()    

            else:
                s.append(a)

        return s  