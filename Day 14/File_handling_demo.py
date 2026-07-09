try:
    file=open("myfile.txt","x")
    print(file)
except Exception as e:
    print(e)

with open("myfile.txt","w") as f:
    f.write("hello")
    print("data added")

with open("myfile.txt","r") as f:
    data=f.read()
    print(data)

with open("myfile.txt","a") as f:
    f.write("\n new data appended")
    print("data appended")

