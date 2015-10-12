def solution(N, A):
    C = [0] * N
    count = 0
    maxi = 0
    for i in A:
        if i <= N:
            if C[i-1] < count:
                C[i-1] = count
            C[i-1] +=  1
            if maxi < C[i-1]:
                maxi = C[i-1]
        else:
            count = maxi
    for j in range(0,N):
        if C[j] < count:
            C[j] = count
    return C
