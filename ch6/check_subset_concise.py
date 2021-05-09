# the concise version of check_subset.py

A = [ x for x in range(5) ]
B = [ x for x in reversed(range(10)) ]

answer = True
for i in A: 
  if A[i] not in B: 
    answer = False

if answer == True:
    print("A is subset of B")
else: 
    print("A is not a subset of B")