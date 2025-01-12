import os
import re
import time

#PART-1 Solution
start=time.time() #to calculate time difference

f=open("hysteria.txt")
lines=f.readlines()
arr1=[]
arr2=[]
dist=[]
sim=[]
arr2_dict={}

for line in lines:

    no=(str(line).replace(" ","").replace("\n",""))
    # no=(str(line).replace("\n",""))
    # print(no)
    arr1.append(no[:5])
    arr2.append(no[5:])
    
arr1.sort()
arr2.sort()

for i in range(len(arr1)):
    diff=int(arr1[i])-int(arr2[i])
    dist.append((abs(diff)))

# print(arr1)
# print(arr2)
# print(dist)
# print("Answer: "+ str(sum(dist)))

for ele in arr2:
    if ele in arr2_dict:
        arr2_dict[ele]=arr2_dict.get(ele)+1
    else:
        arr2_dict[ele]=1

# print(arr2_dict)

for ele in arr1:
    if ele in arr2_dict:
        sim.append(int(ele)*int(arr2_dict.get(ele)))
    else:
        sim.append(0)

print(sum(sim))