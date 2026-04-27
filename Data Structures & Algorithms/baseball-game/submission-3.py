class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        # [5,-2,-4,5,1]
        for i,item in enumerate(operations):
            if  item=='D':
                if stack:
                    newDScore=2*int(stack[-1])
                    stack.append(newDScore)
            elif item=='+':
                if len(stack)>1:
                    newScore=stack[-1]+stack[-2]
                    stack.append(int(newScore))        
            elif item=='C':
                if stack:
                    stack.pop()


            else:
                stack.append(int(item))

        
        return sum(stack)


            
        