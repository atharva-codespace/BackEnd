n = 11
mid = n // 2

for i in range(n):
    for j in range(n):

        if (i == 0 or i == n-1 or      # top & bottom border
            j == 0 or j == n-1 or      # left & right border
            i == mid or                # middle horizontal line
            j == mid or                # middle vertical line
            abs(i-mid) == abs(j-mid)): # center X   i == j or # main diagonal
                                       # i + j == n-1opposite diagonal

            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()