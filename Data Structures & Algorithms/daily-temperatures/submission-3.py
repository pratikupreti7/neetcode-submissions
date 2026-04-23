class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # decreasing stack

        stack=[]
        result=[0]*len(temperatures)

        for i,n in enumerate(temperatures):
            # pop when current > top of stack

            while stack and n>temperatures[stack[-1]]:
                index=stack.pop()
                result[index]=i-index
            
            stack.append(i)
        return result




        