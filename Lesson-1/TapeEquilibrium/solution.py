def solution(A):
    # write your code in Python 2.7
    sum = 0
    for p in A:
        sum = sum + p
    
    q = 0
    for p in range(0,len(A)):
       q = q + A[p]
       diff = abs((sum - q) - q)
       if ( p == 0 ) :
           min = diff
       elif ( diff < min ):
           min = diff
    
    return min
