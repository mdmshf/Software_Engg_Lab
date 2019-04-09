#Program to find cyclometric complexity using predicate node method
# MOHD MUSHARRAF
file_obj=open("musharraf.txt","r")
lookfor = ["if","elif","while","for","try","with","switch"]
c=0
for i in file_obj:
    comment_index=len(i)
    if "#" in i:
        if i.find("#")==0:
            continue
        comment_index=i.find("#")
    for j in lookfor:
        if j in i and ':' in i and i.find(j)<comment_index: 
            c+=1
print("Cyclometric complexity of the given code using predicate node method is : "+str(c))
