import numpy as np
import time
import re

start=time.time()

# #PART 1-SOLUTION
# data_array=np.loadtxt ('xmas.txt',dtype='object')
# data_array=np.array(data_array)
# print(type(data_array))

f=open("xmas.txt")
blob=f.read()
f.close()

key="XMAS"

blob=blob.replace(""," ")

np_array=np.genfromtxt(blob.splitlines(),dtype='U')
print(len(np_array[0]))

#PART 1-SOLUTION

output1=[]
def dotAttachedNumbers(num,lineNo,start,end):
    
    kagi=np.array('.')
    lenOfNum=len(str(num))
    dictOfIndices={
                    'left':[lineNo,(start-1)],
                    'left_diagonal':[(lineNo-1),(start-1)],
                    'left_neg_diagonal':[(lineNo+1),(start-1)],
                    'right':[(lineNo),(end+1)],
                    'right_diagonal':[(lineNo-1),(end+1)],
                    'right_neg_diagonal':[(lineNo+1),(end+1)]
                  }
    for i in range (lenOfNum):
        key1= 'centre_up_'+ str(i)
        key2= 'centre_down_'+str(i)
        dictOfIndices[key1]=[(lineNo-1),(start+i)]
        dictOfIndices[key2]=[(lineNo+1),(start+i)]
  
    for key, value in dictOfIndices.items():
           try:
                  if(value[0]==-1 or value[1]==-1):
                        pass
                  elif((np.char.not_equal(data_array[value[0]][value[1]],kagi))and not(np.char.isdigit(data_array[value[0]][value[1]]))):
                        output1.append(int(num)) 
                        data_array[lineNo]=data_array[lineNo][:start]+('.'*lenOfNum)+data_array[lineNo][(end+1):]
                        break
                  else:
                        data_array[lineNo]=data_array[lineNo][:start]+('.'*lenOfNum)+data_array[lineNo][(end+1):]
           except IndexError:
                  pass
           


for i in range(len(data_array)):
    numbers=re.findall(r'\d+',data_array[i])
    for j in range(len(numbers)):
        
            m=next(re.finditer(numbers[j],data_array[i]))    
            st=(m.start())
            ed=(m.end()-1)
            dotAttachedNumbers(numbers[j],i,st,ed)

print("PART 1 SOLUTION: ",sum(output1))