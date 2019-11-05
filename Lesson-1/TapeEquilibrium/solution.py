def solution(A):
    # write your code in Python 3.6
    # calculate sum
    sum = 0
    for x in A:
        sum += x
    
    # set q to 0
    q = 0
    for i in range(0, len(A)):
        # increment q with next value (move split to next step)
        q += A[i]
        
        # calculate absolute diff between the two parts
        diff = abs(q - (sum - q))
        
        # if its the first time set min to start value
        # else check if min is lesser
        if i == 0 or diff < min:
            min = diff
    return min
    pass
