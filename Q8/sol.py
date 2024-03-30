# Not my proudest solution, although beating 80% of users (exec) (and only 20% regarding memory usage)
# quite simple idea: ascending sort the array, then compare the current elem and the next one --> if they're close (difference <=1) we'll increase the counter.
# Otherwise we'll update the result, if we encountered a longer sequence, then reset the counter

class Solution:

    def sorting(self, nums):
        nums= list(dict.fromkeys(nums))
        nums.sort()
        return nums

    def longestConsecutive(self, nums: List[int]) -> int:
        def sorting(nums):
            nums= list(dict.fromkeys(nums))
            nums.sort()
            return nums
        nums=sorting(nums)
       
        maxi=0
        mix=1
        for idx,j in enumerate(nums):
            
            if idx<len(nums)-1:
                
                if nums[idx+1]-j <= 1:
                    
                    mix+=1
                    
                else:
                    
                    if mix>maxi:
                        maxi=mix
                    mix=1
            else:
                
                if mix>maxi:
                    maxi=mix
                    
        return maxi
    
# BUT, there's a problem: the complexity is O(nlogn), as we require an array sorting... 
    
# Proposed alternative:
    
    class Solution:
        def longestConsecutive(self, nums: List[int]) -> int:
            if not nums:
                return 0

            nums_set = set(nums)

            def find_consecutive(num):
                length = 1
                # Cerca numeri consecutivi più grandi
                next_num = num + 1
                while next_num in nums_set:
                    nums_set.remove(next_num)
                    length += 1
                    next_num += 1
                # Cerca numeri consecutivi più piccoli
                prev_num = num - 1
                while prev_num in nums_set:
                    nums_set.remove(prev_num)
                    length += 1
                    prev_num -= 1
                return length

            max_length = 0
            for num in nums:
                max_length = max(max_length, find_consecutive(num))

            return max_length

# Here we manage to simplify the procedure, and we'll decrease the complexity to O(n), as we initially wanted