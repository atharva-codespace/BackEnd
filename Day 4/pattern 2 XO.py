for i in range(3):
    for j in range(3):
        if i%2==0:
            if j%2==0:
                print("X",end=" ")
            else:
                print("O",end=" ")
        else:
            if j%2==0:
                print("O",end=" ")
            else:
                print("X",end=" ")
    print()