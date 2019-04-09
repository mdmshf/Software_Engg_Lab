# cyclometric complexity using graph method
# MOHD MUSHARRAF


n=8
arr = [[0,0,1,1,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,1,0,1,0],[0,0,0,0,1,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,1,1,0],[0,0,0,0,0,0,0,1],[0,1,0,0,1,0,1,0]]
count=0
for i in arr:
        flag=0
        for j in i:
                if(j==1):
                        flag=1
                        count+=1
        if(flag==1):
                count-=1
count+=1;
print("Cyclometric complexity using graph method = ",count)

