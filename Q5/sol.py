### First approach: brute force, just scroll through the array,
# store in a dictionary how many elems per each 'for' index,
# then just give back the maximum value.
# This method is quite simple, either to understand or to write, but inefficient, as you iterate several times and store useless values.


class Solution:
    def hIndex(self, citations: List[int]) -> int:

       assert 1<=len(citations)<=5000
       a = {}

       for i in range(len(citations)+1):
           
           b=[]
           for j in citations:
               assert 0<=j<=1000
               if j >=1:
                   b.append(j)
           if len(b)>=i:
              a[i]=b
       if len(a.keys()):
           return max(a.keys())
       else: return 1

# In fact, this solution will work, but this doesn't prove at all that you're capable of thinking as a good Software Engineer
# Now, taking inspiration from another LeetCode user (thank you), there is this brilliant strategy
# just order ascendingly, then compare the current value and how many there are in the right part of the list
# (you know they are greater than the current one, as you sorted), get the minimum and select the maximum between it
# and the current h (which starts from 0 and has to be maximized)
       
class Solution:
    def hIndex(self, citations: List[int]) -> int:

        i = 0
        h = 0

        citations.sort()
        while i < len(citations):
            h = max(h,min(citations[i],len(citations) - (i)))
            i += 1

        return h
         
