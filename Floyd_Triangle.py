row=int(input("How many rows?"))
num=1
for i in range(1, row+1):
    for j in range(1,i+1):
        print(num,end= " ")
        num=num+1
    print()

print()      
