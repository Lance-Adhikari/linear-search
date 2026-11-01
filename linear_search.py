A = [8, 3, 12, 5, 9]
k = 5


def linear_search(A, k):
    # Check each element against the target value.
    for i in range(len(A)):
        if k == A[i]:
            # Print every matching index, starting from 0.
            print(i)


linear_search(A, k)
