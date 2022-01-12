array= input("Enter array: ").split(" ")
flag=True
for i in range (len(array)):
    if(array[i]!=array[len(array)-i-1]):
        print("NOT!")
        flag=False
        break

if(flag==True):
    print("YES!")