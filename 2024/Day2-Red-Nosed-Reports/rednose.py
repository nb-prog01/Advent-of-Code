import os
import re
import time
import array

#PART-1 Solution
start=time.time() #to calculate time difference

f=open("rednose.txt")
lines=f.readlines()
arr1=[]
arr2=[]
dist=[]
sim=[]
answer={}
ans=[]

for line in lines:

    no=(str(line).replace("\n",""))
    # no=(str(line).replace("\n",""))
    # print(no)
    a=array.array('i',(int(x) for x in no.split(" ")))
    arr1.append(a)

for ele in arr1:
    # print(ele)
    count=0
    for i in range(len(ele)-1):
        Flag=0
        # print("status: " + str(ele[0]>ele[1]) )
        if(ele[0]>ele[1]):
            # print("inc"+str(ele[0])+" "+str(ele[1]))
            order=ele[i]>ele[i+1]
            # print(str(ele[i])+" "+str(ele[i+1]))
            # print (order)
            diff=abs(ele[i]-ele[i+1])
            # print (diff)
            if(order==True and 0<diff<=3):
                # print("pass1")
                continue
            else:
                # print('notpass1')
                # ans.append('unsafe')
                count+=1
                continue

        elif(ele[0]<ele[1]):
            # print("dec"+str(ele[0])+" "+str(ele[1]))
            order=ele[i]<ele[i+1]
            # print(str(ele[i])+" "+str(ele[i+1]))
            # print (order)
            diff=abs(ele[i]-ele[i+1])
            # print (diff)
            if(order==True and 0<diff<=3):
                # print("pass1")
                continue
            else:
                # print('notpass1')
                # ans.append('unsafe')
                count+=1
                continue
        else:
            # print(ele[0]+" "+ele[1])
            count+=1
            continue
                
    if(count>1):
        Flag=1
        

    print("Count: "+ str(count))
    if (Flag==0):
        # string=' '.join(str(x) for x in ele)
        # print(string)
        ans.append(ele)

print("===========START================")           
print(len(ans))    
print("============END=================")


# with open('rednose1.txt', 'r') as f:
#     content = f.read().strip().split('\n')

# ans = 0
# for report in content:
#     values = list(map(int, report.split()))
#     safepos = set([1, 2, 3])
#     safeneg = set([-1, -2, -3])
#     for i in range(1, len(values)):
#         safepos.add(values[i] - values[i - 1])
#         safeneg.add(values[i] - values[i - 1])

#     if len(safepos) == 3 or len(safeneg) == 3:
        
#         print(report)
#         ans += 1

# print(ans)