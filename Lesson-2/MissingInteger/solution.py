def solution(A):
    n = len(A)
    R = [False] * (n+1)
    for i in A:
        if i > 0 and i <= n:
            R[i] = True
    i = 1
    while i <= n:
        if not R[i]:
            return i
        i += 1
    return (n+1)
