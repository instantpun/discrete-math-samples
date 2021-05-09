# the concise version of check_subset.py

A = [ x for x in range(5) ]
B = [ x for x in reversed(range(10)) ]

answer = "A is a subset of B"
for i in A: 
  if A[i] not in B: 
    answer = "A is not a subset of B"

print(answer)