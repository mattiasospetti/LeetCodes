# Here the main issue behind this question is the O(1) complexity we must respect.
# if it hadn't been there, we could simply use s.reverse(), but with a O(n) complexity,
# as it uses a 'temp' array with the same dimension as input (s)
# https://www.w3schools.com/python/ref_list_reverse.asp


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        assert 1 <= len(s) <= 105 # constraints assertion (check)
        
        for j in range(int(len(s)/2)):

            # We can use a 'tmp' variable used as a temporary store for one elem of the array.
            # the idea here is to get the last and the first elem, store one and switch the other,
            # then cycle to the second couple (second and penultimate elems, and so on...)
            # since we store only one elem, the complexity constraint is respected, quite straightforward.

            tmp=s[j]
            s[j]=s[-j-1]
            s[-j-1]=tmp