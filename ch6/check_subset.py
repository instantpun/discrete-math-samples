# The input set A and B are represented as one-dimensional linked lists whose elements 
# are A[1], A[2], ... , A[n] and B[1], B[2], ... , B[m]
#
# Starting with a A[1] and for each successive A[i] in A, a check is made to see whether
# A[i] is in B. To do this, A[i] is compared to successive element sof B. 
# We let the string answer be set to "A is a subset of B."
# If A[i] is not equal to any element of B, then the output string, called answer is given the value "A is not a subset of B".
# If A[i] equals some element of B, the next successive element in A is checked to see whether it is in B. If every successive element of A
# is found to be in B, then the answer never changes from its initial value of "A is a subset of B."

# Verbose/Explicit algorithm for naively evaluated subsets

A = [ x for x in range(5) ]
B = [ x for x in reversed(range(10)) ]

n = len(A)
m = len(B)

# naive scan detailed in section 6.1.1
answer = "A is subset of B" # default assumption

i = 0
while i < n:
  # need to reset j to zero at every new iteration of the loop, 
  # otherwise A[i] won't be evaluated after the first loop because j > m
  j = 0
  found = False  
  while j < m:
    if A[i] == B[j]:
      found = True
    j = j + 1
  i = i + 1
  if found == False:
    answer = "A is not a subset of B"
    # end loop early because at least one element of A is not in B, no further validation needed
    break