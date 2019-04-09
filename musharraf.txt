#Program to find cyclometric compleiity using concept of region
# MOHD MUSHARRAF
file_obj=open("musharraf.txt","r")

count=0
flag=0
no_of_edges=0
no_of_nodes=0
no_of_exits=1
for i in file_obj:
    comment_index=len(i)
    if "#" in i:
        if i.find("#")==0:
            continue
        comment_index=i.find("#")
    if ("if" in i and "endif" not in i) or "switch" in i or "while" in i:
        if(i.find("if")<comment_index and i.find("switch")<comment_index and i.find("while")<comment_index):
            no_of_edges+=3
            no_of_nodes+=2
    if "=" in i:
        if(i.find("=")<comment_index):
            no_of_edges+=1
            no_of_nodes+=1
    if "cout" in i:
        if(i.find("cout")<comment_index):
            no_of_nodes+=1
    if "for" in i:
        if(i.find("for")<comment_index):
            no_of_edges+=2
            no_of_nodes+=4
    if "return" in i:
        if(i.find("return")<comment_index):
            no_of_exits+=1
    if "endif" in i:
        if(i.find("endif")<comment_index):
            if flag==0:
                flag=1
            else:
                count+=1
    

ans = no_of_edges-no_of_nodes+no_of_exits*2-count
print("Cyclometric complexity of the given code using concept of region is : "+str(ans))
