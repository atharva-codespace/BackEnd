str="Maharastra"
even=0
odd=0

c=len(str)

for i in range(c):
    if i%2==0:
        even+=1
    else:
        odd+=1

print("Even count:",even)
print("Odd count:",odd)