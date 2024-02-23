import os
import re
import time

#PART-1 Solution
start=time.time() #to calculate time difference

f=open("trebuchet.txt")
lines=f.readlines()
arr=[]
sum=0

for line in lines:

    num_index=re.search(r"\d",line).start() #to check first occurance of digit
    num_index2=re.search(r'(\d)[^\d]*$',line).start() #to check last occurance of digit
    no=(str(line[num_index])+str(line[num_index2]))
    arr.append(no)


for i in arr:
    sum=sum+int(i)

print("Part 1 answer: "+str(sum))


#PART-2 Solution

f=open("trebuchet.txt")
lines=f.readlines()
arr=[]
dict={}
sum=0
spell=['one','two','three','four','five','six','seven','eight','nine']
numkey={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
count=0

#Finding spelled numbers and converting them into digits using numkey
#Here we add the number the spelling represents after the first letter of the speling 
#so as to accomodate the merged words (ex: oneight, nineight, eighthree->o1ne8ight,n9ine8ight,e8ight3hree)


for line in lines:
    tempdict={}
    for s in spell:
        temparr=[]
        pat=str(s)
        while(line.find(pat)!=-1):
            temparr.append(line.find(pat))
            line=line.replace(pat,str(pat[:1])+str(numkey[pat])+str(pat[1:]),1)
            
    num_index=re.search(r"\d",line).start()
    num_index2=re.search(r'(\d)[^\d]*$',line).start()
    no=(str(line[num_index])+str(line[num_index2]))
    arr.append(no)       

for i in arr:
    sum=sum+int(i)

print("Part 2 answer: "+str(sum))

End=time.time() #to calculate time difference
print(start)
print(End)
diff=End-start
print("Time taken: "+diff)

