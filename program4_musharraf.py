#program to find function point value
# MOHD MUSHARRAF


ar = [[3,4,6],[4,5,7],[3,4,6],[7,10,15],[5,7,10]]
z=[0 for i in range(5)]
f=[0 for i in range(14)]
x=[0 for i in range(5)]
    

print("Enter User Inputs & its complexity factor (0 for low, 1 for avg, 2 for high) : ")
z[0],x[0]=[int(i) for i in input().split()]
print("Enter User Output & its complexity factor (0 for low, 1 for avg, 2 for high) : ")
z[1],x[1]=[int(i) for i in input().split()]
print("Enter User Inquires & its complexity factor (0 for low, 1 for avg, 2 for high) : ")
z[2],x[2]=[int(i) for i in input().split()]
print("Enter Logical Files & its complexity factor (0 for low, 1 for avg, 2 for high) : ")
z[3],x[3]=[int(i) for i in input().split()]
print("Enter Interface files & its complexity factor (0 for low, 1 for avg, 2 for high) : ")
z[4],x[4]=[int(i) for i in input().split()]
    
print("\n Enter 14 factors in order : \n")
for i in range(14):
    f[i]=int(input())

temp=0
for i in range(14):
    temp+=f[i]
caf = 0.65 + 0.01*temp

ufp=0
for i in range(5):
    ufp+=ar[i][x[i]]*z[i]


fp = caf * ufp;

print("\nFunction point value = ",fp,"\n")

