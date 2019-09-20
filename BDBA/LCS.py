'''
Finding Common subsequence of two strings.

It takes two strings, S1 and S2 at its input and returns the longest common subsequence(LCS) of S1 and S2.

Example:
S1 = "ABAZDC"
S2 = "BACBAD"
LCS = "ABAD"

'''

# 's1' is Given first string.
# 's2' is Given second string.
# 'i1' is Index of 's1'. LCS examine start from Index '0'.
# 'i2' is Index of 's2'. LCS examine start from Index '0'.

#LCS function:
def lcs(s1,s2,i1,i2):
    if i1 == len(s1) or i2 == len(s2):
        return ''
    if s1[i1] == s2[i2]:
        return s1[i1] + lcs(s1,s2,i1+1,i2+1)
    
    result1 = lcs(s1,s2,i1+1,i2)
    result2 = lcs(s1,s2,i1,i2+1)
    
    if len(result1) > len(result2):
        return result1
    else:
        return result2
    
# Calling Function with arguments.
lcs('ABAZDC','BACBAD',0,0)
