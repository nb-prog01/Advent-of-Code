import os
import re
import time

#Bag contains 12 red cubes, 13 green cubes, and 14 blue cubes

#PART-1 Solution
start=time.time() #to calculate time difference
Garr=[]
Rarr=[]
Barr=[]
ans=[]
f=open("cubes.txt")
lines=f.readlines()
count=1
for line in lines:
    #find array of indicies 
    arr1=[m.start() for m in re.finditer('red',line)]
    arr2=[m.start() for m in re.finditer('green',line)]
    arr3=[m.start() for m in re.finditer('blue',line)]


    for i in range(len(arr2)):
        Garr.insert(i,int(line[(int(arr2[i]-3)):(int(arr2[i])-1)]))
    arr2.clear()


    for i in range(len(arr1)):
        Rarr.insert(i,int(line[(int(arr1[i]-3)):(int(arr1[i])-1)]))
    arr1.clear()


    for i in range(len(arr3)):
        Barr.insert(i,int(line[(int(arr3[i]-3)):(int(arr3[i])-1)]))
    arr3.clear()
    

    if ((all(r<=12 for r in Rarr)) and (all(g<=13 for g in Garr)) and (all(b<=14 for b in Barr))):
        ans.append(count)
        Rarr.clear()
        Garr.clear()
        Barr.clear()
    else:
        Rarr.clear()
        Garr.clear()
        Barr.clear()

    count+=1
end=time.time()
print("PART 1: " + str(sum(ans)))
print(end-start)

#PART-2 Solution
start=time.time() #to calculate time difference
Garr=[]
Rarr=[]
Barr=[]
ans=[]
f=open("cubes.txt")
lines=f.readlines()
count=1
for line in lines:
    arr1=[m.start() for m in re.finditer('red',line)]
    arr2=[m.start() for m in re.finditer('green',line)]
    arr3=[m.start() for m in re.finditer('blue',line)]


    for i in range(len(arr2)):
        Garr.insert(i,int(line[(int(arr2[i]-3)):(int(arr2[i])-1)]))

    Gmax=max(Garr)
    arr2.clear()


    for i in range(len(arr1)):
        Rarr.insert(i,int(line[(int(arr1[i]-3)):(int(arr1[i])-1)]))

    Rmax=max(Rarr)
    arr1.clear()


    for i in range(len(arr3)):
        Barr.insert(i,int(line[(int(arr3[i]-3)):(int(arr3[i])-1)]))

    Bmax=max(Barr)
    arr3.clear()
    
    Barr.clear() 
    Garr.clear() 
    Rarr.clear()

    power=(Rmax*Gmax*Bmax)

    ans.append(power)

    count+=1
end=time.time()
print("PART 2: " + str(sum(ans)))
print(end-start)
