players=(
    (1,"Virat",98),
    (2,"Rohit",100),
    (3,"Vaibhav",99),
    (4,"Mahi",101)
)


print("Player Details")
print("---------------------------")
print("ID\tName\tScore")
print("---------------------------")

for p in players:
    print(f"{p[0]}    {p[1]:10} {p[2]}")



max_score = players[0][2]
max_name = players[0][1]

for p in players:
    if p[2] > max_score:
        max_score = p[2]
        max_name = p[1]

print("\nHighest Score Player:")
print(max_name, "-", max_score)



total = 0

for p in players:
    total += p[2]

print("\nTotal Score:", total)



temp = list(players)

temp.sort(key=lambda i:i[2],reverse=True)

print("\nTop 3 Players:")

for i in range(3):
    print(temp[i][1], "-", temp[i][2])