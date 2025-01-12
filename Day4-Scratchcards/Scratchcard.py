import os
import re
import time

start=time.time()

f=open("card.txt")
lines=f.readlines()
temp=[]

points_arr=[]
no_arr=[]

for line in lines:
    points=0
    temp=" ".join(line.split())
    temp=temp.split(":")
    temp=temp[1].split("|")
    temp[0]=temp[0].strip()
    temp[1]=temp[1].strip()
    win_arr=list(map(int,temp[0].split(" ")))
    scratch_arr=list(map(int,temp[1].split(" ")))
    # print(win_arr,"\n",scratch_arr)

    Winset=set(win_arr)
    Scratchset=set(scratch_arr)

    Resset=Winset.intersection(Scratchset)
    no=len(Resset)
    no_arr.append(no)
    print(len(Winset),Winset)
    print(len(Scratchset),Scratchset)
    print(Resset)
    print(no)
    if (no==0):
        points=0
    else:
        points=pow(2,no-1)

    points_arr.append(points)
# print(points_arr)
# print(sum(points_arr))
print(no_arr)