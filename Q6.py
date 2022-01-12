n = int(input("Enter the number: "))
array=[]
for i in range(n):
    array.append([])
    if(i==0):
        array[i].append(1)
    else:
        for j in range(0,i+1):
            if(j==0):
                array[i].append(1)
            elif(j==i):
                array[i].append(1)
            else:
                array[i].append(array[i-1][j]+array[i-1][j-1])
            
    print(array[i])