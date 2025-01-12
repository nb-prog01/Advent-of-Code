import numpy as np
import time
import re

start=time.time()

# #PART 1-SOLUTION
# data_array=np.loadtxt ('Gears.txt',dtype='object',comments=None)
# data_array=np.array(data_array)
# output1=[]
# def dotAttachedNumbers(num,lineNo,start,end):
    
#     kagi=np.array('.')
#     lenOfNum=len(str(num))
#     dictOfIndices={
#                     'left':[lineNo,(start-1)],
#                     'left_diagonal':[(lineNo-1),(start-1)],
#                     'left_neg_diagonal':[(lineNo+1),(start-1)],
#                     'right':[(lineNo),(end+1)],
#                     'right_diagonal':[(lineNo-1),(end+1)],
#                     'right_neg_diagonal':[(lineNo+1),(end+1)]
#                   }
#     for i in range (lenOfNum):
#         key1= 'centre_up_'+ str(i)
#         key2= 'centre_down_'+str(i)
#         dictOfIndices[key1]=[(lineNo-1),(start+i)]
#         dictOfIndices[key2]=[(lineNo+1),(start+i)]
  
#     for key, value in dictOfIndices.items():
#            try:
#                   if(value[0]==-1 or value[1]==-1):
#                         pass
#                   elif((np.char.not_equal(data_array[value[0]][value[1]],kagi))and not(np.char.isdigit(data_array[value[0]][value[1]]))):
#                         output1.append(int(num)) 
#                         data_array[lineNo]=data_array[lineNo][:start]+('.'*lenOfNum)+data_array[lineNo][(end+1):]
#                         break
#                   else:
#                         data_array[lineNo]=data_array[lineNo][:start]+('.'*lenOfNum)+data_array[lineNo][(end+1):]
#            except IndexError:
#                   pass
           


# for i in range(len(data_array)):
#     numbers=re.findall(r'\d+',data_array[i])
#     for j in range(len(numbers)):
        
#             m=next(re.finditer(numbers[j],data_array[i]))    
#             st=(m.start())
#             ed=(m.end()-1)
#             dotAttachedNumbers(numbers[j],i,st,ed)

# print("PART 1 SOLUTION: ",sum(output1))


# #PART-2 SOLUTION
# data_array=np.loadtxt ('Gears.txt',dtype='object',comments=None)
# data_array=np.array(data_array)
# output={}

# def starAttachedNumbers(num,lineNo,start,end):
    
#     kagi=np.array('*')
#     lenOfNum=len(str(num))
#     dictOfIndices={
#                     'left':[lineNo,(start-1)],
#                     'left_diagonal':[(lineNo-1),(start-1)],
#                     'left_neg_diagonal':[(lineNo+1),(start-1)],
#                     'right':[(lineNo),(end+1)],
#                     'right_diagonal':[(lineNo-1),(end+1)],
#                     'right_neg_diagonal':[(lineNo+1),(end+1)]
#                   }
#     for i in range (lenOfNum):
#         key1= 'centre_up_'+ str(i)
#         key2= 'centre_down_'+str(i)
#         dictOfIndices[key1]=[(lineNo-1),(start+i)]
#         dictOfIndices[key2]=[(lineNo+1),(start+i)]
  
#     for key, value in dictOfIndices.items():
#            try:
#                   if(value[0]==-1 or value[1]==-1):
#                         pass
#                   elif(np.char.equal(data_array[value[0]][value[1]],kagi)):
#                          index_key=str(value[0]+1)+','+str(value[1]+1)
#                          if index_key in output:
                                
#                                 output[index_key].append(num)
#                                 data_array[lineNo]=data_array[lineNo][:start]+('.'*lenOfNum)+data_array[lineNo][(end+1):]
                        
#                          else:
                                
#                                 output[index_key]=[]
#                                 output[index_key].append(num)
#                                 data_array[lineNo]=data_array[lineNo][:start]+('.'*lenOfNum)+data_array[lineNo][(end+1):]
#                   else:
#                         data_array[lineNo]=data_array[lineNo][:start]+('.'*lenOfNum)+data_array[lineNo][(end+1):]
#            except IndexError:
#                   pass
           


# for i in range(len(data_array)):
#     numbers=re.findall(r'\d+',data_array[i])
#     for j in range(len(numbers)):
        
#             m=next(re.finditer(numbers[j],data_array[i]))    
#             st=(m.start())
#             ed=(m.end()-1)
#             starAttachedNumbers(numbers[j],i,st,ed)

# gear_ratio=[]

# for key,value in output.items():
#       if (len(value)==2):
#             gear_ratio.append(int(value[0])*int(value[1]))

# print("PART 2 SOLUTION: ",sum(gear_ratio))

import re
from operator import mul

with open('Gears.txt', 'r') as f:
    puzzle_input = f.read()


def part1(puzzle_input):

    lines = puzzle_input.split('\n')

    symbol_regex = r'[^.\d]'
    symbol_adjacent = set()
    for i, line in enumerate(lines):
        for m in re.finditer(symbol_regex, line):
            j = m.start()
            symbol_adjacent |= {(r, c) for r in range(i-1, i+2) for c in range(j-1, j+2)}

    number_regex = r'\d+'
    part_num_sum = 0
    for i, line in enumerate(lines):
        for m in re.finditer(number_regex, line):
            if any((i, j) in symbol_adjacent for j in range(*m.span())):
                part_num_sum += int(m.group())

    return part_num_sum


def part2(puzzle_input):
    lines = puzzle_input.split('\n')

    gear_regex = r'\*'
    gears = dict()
    for i, line in enumerate(lines):
        for m in re.finditer(gear_regex, line):
            gears[(i, m.start())] = []

    number_regex = r'\d+'
    for i, line in enumerate(lines):
        for m in re.finditer(number_regex, line):
            for r in range(i-1, i+2):
                for c in range(m.start()-1, m.end()+1):
                    if (r, c) in gears:
                        gears[(r, c)].append(int(m.group()))

    gear_ratio_sum = 0
    for nums in gears.values():
        if len(nums) == 2:
            gear_ratio_sum += mul(*nums)

    return gear_ratio_sum



print('Part 1:', part1(puzzle_input))
print('Part 2:', part2(puzzle_input))

end=time.time()
print("Time taken: "+str(end-start)+" seconds")
