def solution(A):
    n = len(A)
    count = 0
    R = [False] * (n+1)
    for i in range(0,n):
        if A[i] > n:
            return 0
        if not R[A[i]]:
            count += 1
            R[A[i]] = True
        else:
            return 0
    if count == n:
        return 1
    else:
        return 0
