n = int(input("How many terms do you want in your Fibonacci Series: "))

a=0
b=1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c