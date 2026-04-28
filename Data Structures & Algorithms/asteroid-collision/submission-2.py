class Solution:
    def asteroidCollision(self, nums: List[int]) -> List[int]:

        stack=[]
        # [2,4,-4,-1]
            #  2 ,4 ,
            # 2 -4 collide

        for num in nums:
            # appending in stack
            while stack and num<0 and stack[-1]>0:
                diff= stack[-1]+num

                if diff <0:
                    stack.pop()
                elif diff>0:
                    num=0
                else:
                    num=0
                    stack.pop()

            if num:
                stack.append(num)
        return stack

    

        