class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        n=len(arr)
        max_right=arr[n-1] #2
        arr[n-1]=-1 #
        for i in range(n-2,-1,-1):
            org=arr[i]
            arr[i]=max_right
            max_right=max(max_right,org)
            

            

        return arr



        