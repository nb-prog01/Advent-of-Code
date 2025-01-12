import numpy as np
import time
import regex as re

start=time.time()

# #PART 1-SOLUTION
data_array=np.loadtxt ('xmas.txt',dtype='object')
data_array=np.array(data_array)
print(type(data_array))

key="XMAS"
HCOUNT=0
VCOUNT=0
LDCOUNT=0
RDCOUNT=0

vertical=np.empty(shape=(140,140),dtype='object')
horizontal=np.empty(shape=(140,140),dtype='object')

f=open("xmas.txt")
blob=f.read()
blob=blob.replace(""," ")

np_array=np.genfromtxt(blob.splitlines(),dtype='U')
# print(np_array)

for i in range(len(data_array)):
      for j in range(len(data_array)):
            vertical[j][i]=str(data_array[i][j])

horizontal=np.rot90(np.fliplr(vertical))

for i in range(len(horizontal)):
      x_str=''.join(str(a) for a in horizontal[i])
      # print(x_str)
      pattern=r"XMAS|SAMX"
      matches=re.findall(pattern,x_str,overlapped=True)
      # print(matches)
      HCOUNT+=len(matches)

print("Horizontal count:",HCOUNT)

for i in range(len(vertical)):
      x_str=''.join(str(a) for a in vertical[i])
      # print(x_str)
      pattern=r"XMAS|SAMX"
      matches=re.findall(pattern,x_str,overlapped=True)
      # print(matches)
      VCOUNT+=len(matches)

print("Vertical count:",VCOUNT)

#left to right diagonal
for i in range(-np_array.shape[0]+1,np_array.shape[0]):
      olo=np_array.diagonal(offset=i)
      x_str=''.join(str(a) for a in olo)
      # print(x_str)
      pattern=r"XMAS|SAMX"
      matches=re.findall(pattern,x_str,overlapped=True)
      # print(matches)
      LDCOUNT+=len(matches)

print("LD count:",LDCOUNT)

#right to left diagonal

diagonalmat=np.rot90(horizontal)

for i in range(-horizontal.shape[0]+1,horizontal.shape[0]):
      polo=diagonalmat.diagonal(offset=i)
      x_str=''.join(str(a) for a in polo)
      # print(x_str)
      pattern=r"XMAS|SAMX"
      matches=re.findall(pattern,x_str,overlapped=True)
      # print(matches)
      RDCOUNT+=len(matches)

print("RD count:",RDCOUNT)


sum=HCOUNT+VCOUNT+LDCOUNT+RDCOUNT
print(sum)


print("===========================================================")
end=time.time()
print("Time taken: "+str(end-start)+" seconds")