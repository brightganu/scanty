print("Program to print half pyramid: ")
rows = input("Enter number of rows ")
rows = int (rows)
for i in range (rows,0,-1):
    for j in range(0, i + 1):
        print(j, end=' ')
    print("\r")