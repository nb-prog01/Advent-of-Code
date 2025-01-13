import numpy as np
import time
import regex as re

start=time.time()

# #PART 1-SOLUTION
data_array=np.loadtxt ('xmas.txt',dtype='object')
data_array=np.array(data_array)
print((data_array))

HCOUNT=0
VCOUNT=0
LDCOUNT=0
RDCOUNT=0

vertical=np.empty(shape=(140,140),dtype='object')
horizontal=np.empty(shape=(140,140),dtype='object')

# f=open("xmas.txt")
# blob=f.read()
# blob=blob.replace(""," ")

# np_array=np.genfromtxt(blob.splitlines(),dtype='U')
# # print(np_array)

# for i in range(len(data_array)):
#       for j in range(len(data_array)):
#             vertical[j][i]=str(data_array[i][j])

# horizontal=np.rot90(np.fliplr(vertical))

# for i in range(len(horizontal)):
#       x_str=''.join(str(a) for a in horizontal[i])
#       # print(x_str)
#       pattern=r"XMAS|SAMX"
#       matches=re.findall(pattern,x_str,overlapped=True)
#       # print(matches)
#       HCOUNT+=len(matches)

# print("Horizontal count:",HCOUNT)

# for i in range(len(vertical)):
#       x_str=''.join(str(a) for a in vertical[i])
#       # print(x_str)
#       pattern=r"XMAS|SAMX"
#       matches=re.findall(pattern,x_str,overlapped=True)
#       # print(matches)
#       VCOUNT+=len(matches)

# print("Vertical count:",VCOUNT)

# #left to right diagonal
# for i in range(-np_array.shape[0]+1,np_array.shape[0]):
#       olo=np_array.diagonal(offset=i)
#       x_str=''.join(str(a) for a in olo)
#       # print(x_str)
#       pattern=r"XMAS|SAMX"
#       matches=re.findall(pattern,x_str,overlapped=True)
#       # print(matches)
#       LDCOUNT+=len(matches)

# print("LD count:",LDCOUNT)

# #right to left diagonal

# diagonalmat=np.rot90(horizontal)

# for i in range(-horizontal.shape[0]+1,horizontal.shape[0]):
#       polo=diagonalmat.diagonal(offset=i)
#       x_str=''.join(str(a) for a in polo)
#       # print(x_str)
#       pattern=r"XMAS|SAMX"
#       matches=re.findall(pattern,x_str,overlapped=True)
#       # print(matches)
#       RDCOUNT+=len(matches)

# print("RD count:",RDCOUNT)


# sum=HCOUNT+VCOUNT+LDCOUNT+RDCOUNT
# print("PART 1 SOLUTION: ",sum)


output1=[]
def dotAttachedNumbers(lineNo,col):
    
    M=np.array('M')
    S=np.array('S')
    Flag1=0
    Flag2=0
    dictOfIndices1={
                    'left_diagonal':[[(lineNo-1),(col-1)],[(lineNo+1),(col+1)]]
                  }
    dictOfIndices2={
                    'left_neg_diagonal':[[(lineNo+1),(col-1)],[(lineNo-1),(col+1)]]
                  }    
  
    for key, value in dictOfIndices1.items():
           try:
                  if(value[0]==-1 or value[1]==-1):
                        pass
                  elif(((np.char.equal(data_array[value[0][0]][value[0][1]],M))and(np.char.equal(data_array[value[1][0]][value[1][1]],S)))or((np.char.equal(data_array[value[0][0]][value[0][1]],S))and(np.char.equal(data_array[value[1][0]][value[1][1]],M)))):
                        Flag1=1 
                        print(data_array[value[0][0]][value[0][1]],'A',data_array[value[1][0]][value[1][1]])
                        # data_array[lineNo]=data_array[lineNo][:start]+('.'*lenOfNum)+data_array[lineNo][(end+1):]
                        break
                  # else:
                        # data_array[lineNo]=data_array[lineNo][:start]+('.'*lenOfNum)+data_array[lineNo][(end+1):]
           except IndexError:
                  pass
           
    for key, value in dictOfIndices2.items():
           try:
                  if(value[0]==-1 or value[1]==-1):
                        pass
                  elif(((np.char.equal(data_array[value[0][0]][value[0][1]],M))and(np.char.equal(data_array[value[1][0]][value[1][1]],S)))or((np.char.equal(data_array[value[0][0]][value[0][1]],S))and(np.char.equal(data_array[value[1][0]][value[1][1]],M)))):
                        Flag2=1
                        print(data_array[value[0][0]][value[0][1]],'A',data_array[value[1][0]][value[1][1]]) 
                        # data_array[lineNo]=data_array[lineNo][:start]+('.'*lenOfNum)+data_array[lineNo][(end+1):]
                        break
                  # else:
                        # data_array[lineNo]=data_array[lineNo][:start]+('.'*lenOfNum)+data_array[lineNo][(end+1):]
           except IndexError:
                  pass
           
    if(Flag1==1 and Flag2==1):
          output1.append(1)
          
          

           


for i in range(len(data_array)):
      for j in range(len(data_array)):
            if(str(data_array[i][j])=='A'):
                  dotAttachedNumbers(i,j)

#     numbers=re.findall(r'A',data_array[i])
#     print(numbers)
#     for j in range(len(numbers)):
        
#             m=next(re.finditer(numbers[j],data_array[i]))    
#             st=(m.start())
#             ed=(m.end()-1)
#             print(st,ed)
#             dotAttachedNumbers(numbers[j],i,st,ed)

print("PART 1 SOLUTION: ",sum(output1))




print("===========================================================")
end=time.time()
print("Time taken: "+str(end-start)+" seconds")