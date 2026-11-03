print("Half Pyramid Pattern")
row = int(input("Enter number of rows"))
num=1
for r in range(1,row+1):
    for j in range(1,r+1):
        print(num,end="  ")
        num+=1

    print()