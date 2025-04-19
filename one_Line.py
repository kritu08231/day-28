#print the one line of the list
n=int(input("Enter the number"))
matrix=[]
for i in range(n):
    matrix.append([int(ele)for ele in input().split()])
trace=[]
for i in range(n):
    trace.append(matrix[i][i])
print(trace)
