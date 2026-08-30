class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # space : O(n)
        '''
        n = len(nums)
        # normalize k for k right side rotation
        k = k % n
        temp = nums[:] # copy current array

        for i in range(n):
            # exact roation position will be for k step : (i+k) % n
            new_index = (i + k)%n
            nums[new_index] = temp[i]
    
        '''

        # space : O(1) 
        # ideal approach 
        # 1. reverse whole 2. reverse first k 3. reverse remaining from k to n
        # [1,2,3,4] => [4,3,2,1] => k= 2 and [3,4,2,1] => [3,4,1,2]

        n = len(nums)
        k = k % n # normalization
        def reverse(s,e):
            while s < e:
                nums[s], nums[e] = nums[e], nums[s]
                s += 1
                e -= 1
            
        # whole 
        reverse(0, n-1)
        # fist k
        reverse(0, k-1)
        # remaining
        reverse(k, n-1)


            


        