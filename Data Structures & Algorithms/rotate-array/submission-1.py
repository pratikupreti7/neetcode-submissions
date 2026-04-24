class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # [1,2,3,4,5,6,7,8]
        # 0-k-1 k-n
        # 1 2 3 4     5 6 7 8
        # 4 3 2 1.    8 7 6 5
        # 56781234
        n = len(nums)
        k %= n
        def reverse(arr,start,end):

            while start<end:
                arr[start],arr[end]=arr[end],arr[start]
                start+=1
                end-=1
            
        reverse(nums, 0, n - 1)      # whole first
        reverse(nums, 0, k - 1)      # then first k
        reverse(nums, k, n - 1)      # then last n-k

            

    

    
        