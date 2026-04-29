class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]

        for num in asteroids:
            
            # collide in opp direction
            while stack and num<0 and stack[-1]>0:
                diff=stack[-1]+num
                if diff>0:
                    num=0
                elif diff<0:
                    stack.pop()
                else:
                    num=0
                    stack.pop()

            if num:
                stack.append(num)

        return stack




        