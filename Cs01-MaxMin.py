num = int(input("Enter Your Loop:"))
total=[]
for i in range(num):
    data=int(input("Enter Your Number:"))
    total+=[data]

x=(min(total))
y=(max(total))
print(x)
print(y)