stud={
    101:{"Name":"Ram",
          "Age":18,
          "Subjects":["Python","Java","Mern_stack"],
          "Marks":[30,89,78]
        },
    102:{"Name":"Sita",
          "Age":19,
          "Subjects":["Python","Java","Mern_stack"],
          "Marks":[70,80,90]
        },
     103:{"Name":"Rahul",
          "Age":20,
          "Subjects":["Python","Java","Mern_stack"],
          "Marks":[58,79,90]
        },
     104:{"Name":"Gita",
          "Age":11,
          "Subjects":["Python","Java","Mern_stack"],
          "Marks":[89,97,100]
        }
}

lis=[]

print("-------------------------------------------------------------------------")
print("List of all students with total marks:")
print("-------------------------------------------------------------------------")
print("Roll No\tName\tAge\t  \tSubjects\t\t\t  Marks\t\tTotal")
for key,val in stud.items():  
    for v in val.values():
        if type(v) == list and type(v[0]) == int:
            total=0
            for i in v:
                total+=i
            lis.append([total,key,val["Name"],val["Marks"],val["Age"]])
    print(f"{key}\t{val['Name']}\t{val['Age']}\t{val['Subjects']}\t{val['Marks']}\t{total}")

print("-------------------------------------------------------------------------")
lis.sort(reverse=True)
print("Topper from the above list of students is:")
print("RollNo\tName\tTotal")
print(lis[0][1],"   " ,lis[0][2], "   ",lis[0][0])
print("-------------------------------------------------------------------------")
print("Name of the student who has Highest score in Python:")
lis.sort( key=lambda  i:i[3],reverse=True)
print("RollNo\tName\tMarks in Python")
print(lis[0][1],"   ",lis[0][2],"\t",lis[0][3][0])
print("-------------------------------------------------------------------------")
print("Name of the students who has ag greater that 19 are:")
print("Rollno\tName\tAge")
for i in range(len(lis)):
    if lis[i][4]>19:
        print(lis[i][1],"   ",lis[i][2],"\t",lis[i][4])
print("-------------------------------------------------------------------------")
print("Name of the students having marks between 70-90 in MERN Stack are:")
print("Rollno\tName\tMarks in MERN Stack")
for i in lis:
    if 70 < i[3][2] < 90:
        print(i[1],"   ",i[2],"\t",i[3][2])


