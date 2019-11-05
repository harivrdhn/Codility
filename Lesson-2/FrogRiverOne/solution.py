def solution(X, A):
    # write your code in Python 3.6
    
    # if river is 0, return.
    if X == 0:
        return 0
    # if number of keaves less than river, return
    elif  len(A) < X:
        return -1
    
    # array of places
    places = [False] * (X + 1)
    i = 0
    for k in range(0, len(A)):
        if not places[A[k]]: # if no leaf in place
            places[A[k]] = True
            i += 1 # increment count
            if i == X: # if count and places are equal, we have leaf in each place
                return k
    return -1
    pass
