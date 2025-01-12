import os
import re
import time

#PART-1 Solution
start=time.time() #to calculate time difference

f=open("mull.txt")
blob=f.read()
f.close()
# blob=blob.replace("\\n","-----NEWLINE-----")
blob+="thisistheend"
# print(blob)
out=[]
print(type(blob))
# print(blob)

do="do()"
dont="don't()"
end="thisistheend"
d=str(re.escape(do))
dn=str(re.escape(dont))
end=str(re.escape(end))


newblob=re.sub(f'{dn}((.)*?){d}','+++replaced+++',blob,flags=re.DOTALL)
# print(newblob)
newblob1=re.sub(f'{dn}(.*){end}','+++replaced+++',newblob,flags=re.DOTALL)
print("+++++++++++++++++++++++++++++")
print(newblob1)
print("+++++++++++++++++++++++++++++")
pattern=r"mul\(\d{1,3},\d{1,3}\)"
# pattern=r"don't\(\)"
matches=re.findall(pattern,newblob1)
print (len(matches))
for ele in matches:
    pat=r"\d{1,3}"
    mat=re.findall(pat,ele)
    multiplcation=(int(mat[0])*int(mat[1]))
    out.append(multiplcation)
print("-----------------------------")
print(sum(out))
    