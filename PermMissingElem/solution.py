def solution(A):
    total = 0
    for i in A:
        total += int(i)
    sum = ((len(A)+1)*(len(A)+2))/2
    return sum - total
