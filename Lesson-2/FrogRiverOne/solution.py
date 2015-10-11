def solution(X, A):
    R = [False]* (X+1)
    count = 0
    for i in range (0,len(A)):
        if not R[A[i]]:
            count += 1
            R[A[i]] = True
        if count == X:
            return i
    return -1
