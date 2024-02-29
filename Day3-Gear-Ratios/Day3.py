import numpy as np
import os
import time
import pandas as pd
import re



start=time.time()

'''
NW    N    NE

W     D    E

SW    S    SE

D= [row][col]
N= [row-1][col]
E= [row][col+1]
W= [row][col-1]
S= [row+1][col]
NW=[row-1][col-1]
NE=[row-1][col+1]
SW=[row+1][col-1]
SE=[row+1][col+1]

'''
data=np.loadtxt ('Gears.txt',dtype='object',comments=None)
data=np.array(data)
temp_data=[]
print(len(data))
num_indices=[]

dot=np.array('.')
output=[]
print("lines: "+str(len(data)))

for i in range(len(data)):
    numbers=re.findall(r'\d+',data[i])

    for j in range(len(numbers)):
        
            m=next(re.finditer(numbers[j],data[i]))    
            print((m))
            st=(m.start())
            ed=(m.end()-1)
            print (i,st,ed)
            #conditon for top row inbetween cols inbetween data
            if((i==0) and st>0 and ed<((len(data[i]))-1)):
                print("inside i==0")
                numcheck=np.char.isdigit(data[i+1][st])
                dotcheck=np.char.equal(data[i+1][st],dot)
                dotcheck_side=np.char.equal(data[i][st-1],dot)
                dotcheckcentredown=np.char.equal(data[i+1][st+1],dot)
                dotcheck_leftdown=np.char.equal(data[i+1][st-1],dot)
            
                dotcheck_rightdown=np.char.equal(data[i+1][ed+1],dot)
                dotcheckendside=np.char.equal(data[i][ed+1],dot)

                numcheck1=np.char.isdigit(data[i+1][ed])
                dotcheck1=np.char.equal(data[i+1][ed],dot)

                if((numcheck==False and dotcheck==False) or dotcheckcentredown==False or dotcheck_side==False or dotcheck_leftdown==False or dotcheck_rightdown==False or dotcheckendside==False or dotcheck1==False):
                    print("found a special character"+str(numbers[j]))
                    output.append(int(numbers[j]))
                    # data[i]=data[i][:st]+('.'*len(numbers[j]))+data[i][(ed+1):]
                    
                    data[i]=data[i][:st]+('.'*len(numbers[j]))+data[i][(ed+1):]
                    print(data[i])
                else:
                        data[i]=data[i][:st]+('.'*len(numbers[j]))+data[i][(ed+1):]
                        print(data[i])
            
            #condition for in btwn rows cols
            elif(0<i and i<(len(data)-1) and st>0 and ed<(len(data[i])-1)):
                print("inside 0<i<len(data)")
                numcheck_prev=np.char.isdigit(data[i-1][st])
                dotcheck_prev=np.char.equal(data[i-1][st],dot)
                numcheck_next=np.char.isdigit(data[i+1][st])
                dotcheck_next=np.char.equal(data[i+1][st],dot)
                dotcheck_side=np.char.equal(data[i][st-1],dot)
                dotcheck_leftup=np.char.equal(data[i-1][st-1],dot)
                dotcheck_leftdown=np.char.equal(data[i+1][st-1],dot)
                dotcheck_rightup=np.char.equal(data[i-1][ed+1],dot)
                dotcheck_rightdown=np.char.equal(data[i+1][ed+1],dot)
                dotcheck1=np.char.equal(data[i+1][ed],dot)
                dotcheck2=np.char.equal(data[i-1][ed],dot)
                dotcheckcentreup=np.char.equal(data[i-1][st+1],dot)
                dotcheckcentredown=np.char.equal(data[i+1][st+1],dot)
                dotcheckendside=np.char.equal(data[i][ed+1],dot)
                if((numcheck_prev==False and dotcheck_prev==False) or
                    (numcheck_next==False and dotcheck_next==False) or
                      dotcheck_side==False or dotcheck_leftup==False or
                        dotcheck_leftdown==False or
                          dotcheck_rightup==False or
                            dotcheck_rightdown==False or
                              dotcheck1==False or
                                dotcheck2==False or
                                  dotcheckcentreup==False or
                                    dotcheckcentredown==False or
                                    dotcheckendside==False):
                                    print("found a special character"+str(numbers[j]))
                                    output.append(int(numbers[j]))
                                    data[i]=data[i][:st]+('.'*len(numbers[j]))+data[i][(ed+1):]
                                    print(data[i])
                else:
                    data[i]=data[i][:st]+('.'*len(numbers[j]))+data[i][(ed+1):]
                    print(data[i])

            #confition for bottom row inbetween columns
            elif(i==(len(data)-1) and st>0 and ed<(len(data[i])-1)):
                print("inside i==len(data)")
                numcheck_prev=np.char.isdigit(data[i-1][st])
                dotcheck_prev=np.char.equal(data[i-1][st],dot)

                dotcheck_side=np.char.equal(data[i][st-1],dot)
                dotcheck_leftup=np.char.equal(data[i-1][st-1],dot)
 
                dotcheck_rightup=np.char.equal(data[i-1][ed+1],dot)
    
                # dotcheck1=np.char.equal(data[i+1][ed],dot)
                dotcheck2=np.char.equal(data[i-1][ed],dot)
                dotcheckcentreup=np.char.equal(data[i-1][st+1],dot)
                dotcheckendside=np.char.equal(data[i][ed+1],dot)

                if((numcheck_prev==False and dotcheck_prev==False) or
                    
                      dotcheck_side==False or
                        dotcheck_leftup==False or
                        
                          dotcheck_rightup==False or
                            
                              
                                dotcheck2==False or
                                  dotcheckcentreup==False or
                                    
                                    dotcheckendside==False):
                                    print("found a special character"+str(numbers[j]))
                                    output.append(int(numbers[j]))
                                    data[i]=data[i][:st]+('.'*len(numbers[j]))+data[i][(ed+1):]
                                    print(data[i])
                else:
                    data[i]=data[i][:st]+('.'*len(numbers[j]))+data[i][(ed+1):]
                    print(data[i])
            #condition for left col most top row
                                    
            elif(i==0 and st==0 and ed<len(data[i])):
                print("inside i==0 st==0")
                numcheck=np.char.isdigit(data[i+1][st])
                dotcheck=np.char.equal(data[i+1][st],dot)
                
                dotcheck_rightdown=np.char.equal(data[i+1][ed+1],dot)
                dotcheckendside=np.char.equal(data[i][ed+1],dot)

                numcheck1=np.char.isdigit(data[i+1][ed])
                dotcheck1=np.char.equal(data[i+1][ed],dot)

                if((numcheck==False and dotcheck==False) or dotcheck_rightdown==False or dotcheckendside==False or dotcheck1==False):
                    print("found a special character"+str(numbers[j]))
                    output.append(int(numbers[j]))
                    data[i]=data[i][:st]+('.'*len(numbers[j]))+data[i][(ed+1):]
                    print(data[i])
                else:
                        data[i]=data[i][:st]+('.'*len(numbers[j]))+data[i][(ed+1):]
                        print(data[i])

            #condition for left col most bottom row
                    
            elif(i==(len(data)-1) and st==0 and ed<len(data[i])):
                print("inside i==len(data) st==0")
                numcheck_prev=np.char.isdigit(data[i-1][st])
                dotcheck_prev=np.char.equal(data[i-1][st],dot)
 
                dotcheck_rightup=np.char.equal(data[i-1][ed+1],dot)
    
                
                dotcheck2=np.char.equal(data[i-1][ed],dot)
                dotcheckcentreup=np.char.equal(data[i-1][st+1],dot)
                dotcheckendside=np.char.equal(data[i][ed+1],dot)

                if((numcheck_prev==False and dotcheck_prev==False) or
                        
                          dotcheck_rightup==False or
                            
                              
                                dotcheck2==False or
                                  dotcheckcentreup==False or
                                    
                                    dotcheckendside==False):
                                    print("found a special character"+str(numbers[j]))
                                    output.append(int(numbers[j]))
                                    data[i]=data[i][:st]+('.'*len(numbers[j]))+data[i][(ed+1):]
                                    print(data[i])
                else:
                        data[i]=data[i][:st]+('.'*len(numbers[j]))+data[i][(ed+1):]
                        print(data[i]) 
            #condition for left col most inbetween row
            elif(0<i and i<(len(data)-1) and st==0 and ed<len(data[i])):
                print("inside 0<i<len(data) st==0")
                numcheck_prev=np.char.isdigit(data[i-1][st])
                dotcheck_prev=np.char.equal(data[i-1][st],dot)
                numcheck_next=np.char.isdigit(data[i+1][st])
                dotcheck_next=np.char.equal(data[i+1][st],dot)
                # dotcheck_side=np.char.equal(data[i][st-1],dot)
                # dotcheck_leftup=np.char.equal(data[i-1][st-1],dot)
                # dotcheck_leftdown=np.char.equal(data[i+1][st-1],dot)
                dotcheck_rightup=np.char.equal(data[i-1][ed+1],dot)
                dotcheck_rightdown=np.char.equal(data[i+1][ed+1],dot)
                dotcheck1=np.char.equal(data[i+1][ed],dot)
                dotcheck2=np.char.equal(data[i-1][ed],dot)
                dotcheckcentreup=np.char.equal(data[i-1][st+1],dot)
                dotcheckcentredown=np.char.equal(data[i+1][st+1],dot)
                dotcheckendside=np.char.equal(data[i][ed+1],dot)
                if((numcheck_prev==False and dotcheck_prev==False) or
                    (numcheck_next==False and dotcheck_next==False) or
                      
                        
                          dotcheck_rightup==False or
                            dotcheck_rightdown==False or
                              dotcheck1==False or
                                dotcheck2==False or
                                  dotcheckcentreup==False or
                                    dotcheckcentredown==False or
                                    dotcheckendside==False):
                                    print("found a special character"+str(numbers[j]))
                                    output.append(int(numbers[j]))
                                    data[i]=data[i][:st]+('.'*len(numbers[j]))+data[i][(ed+1):]
                                    print(data[i])
                else:
                        data[i]=data[i][:st]+('.'*len(numbers[j]))+data[i][(ed+1):]
                        print(data[i])
            #condition for right col most top row
            elif(i==0 and st>0 and ed==((len(data[i]))-1)):
                print("inside i==0 ed==len(data)")
                numcheck=np.char.isdigit(data[i+1][st])
                dotcheck=np.char.equal(data[i+1][st],dot)
                dotcheck_side=np.char.equal(data[i][st-1],dot)
                
                dotcheck_leftdown=np.char.equal(data[i+1][st-1],dot)
            
                # dotcheck_rightdown=np.char.equal(data[i+1][ed+1],dot)
                # dotcheckendside=np.char.equal(data[i][ed+1],dot)

                numcheck1=np.char.isdigit(data[i+1][ed])
                dotcheck1=np.char.equal(data[i+1][ed],dot)

                if((numcheck==False and dotcheck==False) or dotcheck_side==False or dotcheck_leftdown==False or dotcheck1==False):
                    print("found a special character"+str(numbers[j]))
                    output.append(int(numbers[j]))
                    data[i]=data[i][:st]+('.'*len(numbers[j]))+data[i][(ed+1):]
                    print(data[i])
                else:
                        data[i]=data[i][:st]+('.'*len(numbers[j]))+data[i][(ed+1):]
                        print(data[i])
            #condition for right col most bottom row
                    
            elif(i==((len(data))-1) and st>0 and ed==((len(data[i]))-1)):
                print("inside i==len(data) ed==len(data)")
                numcheck_prev=np.char.isdigit(data[i-1][st])
                dotcheck_prev=np.char.equal(data[i-1][st],dot)

                dotcheck_side=np.char.equal(data[i][st-1],dot)
                dotcheck_leftup=np.char.equal(data[i-1][st-1],dot)
 
                # dotcheck_rightup=np.char.equal(data[i-1][ed+1],dot)
    
                # dotcheck1=np.char.equal(data[i+1][ed],dot)
                dotcheck2=np.char.equal(data[i-1][ed],dot)
                dotcheckcentreup=np.char.equal(data[i-1][st+1],dot)
                # dotcheckendside=np.char.equal(data[i][ed+1],dot)

                if((numcheck_prev==False and dotcheck_prev==False) or
                    
                      dotcheck_side==False or
                        dotcheck_leftup==False or
                        
                          
                            
                              
                                dotcheck2==False or
                                  dotcheckcentreup==False
                                    
                                    ):
                                    print("found a special character"+str(numbers[j]))
                                    output.append(int(numbers[j]))
                                    data[i]=data[i][:st]+('.'*len(numbers[j]))+data[i][(ed+1):]
                                    print(data[i])
                else:
                        data[i]=data[i][:st]+('.'*len(numbers[j]))+data[i][(ed+1):]
                        print(data[i])
            #condition for right col most inbetween row
            elif(0<i and i<(len(data)-1) and st>0 and ed==((len(data[i]))-1)):
                print("inside 0<i<len(data) ed==len(data[i])")
                numcheck_prev=np.char.isdigit(data[i-1][st])
                dotcheck_prev=np.char.equal(data[i-1][st],dot)
                numcheck_next=np.char.isdigit(data[i+1][st])
                dotcheck_next=np.char.equal(data[i+1][st],dot)
                dotcheck_side=np.char.equal(data[i][st-1],dot)
                dotcheck_leftup=np.char.equal(data[i-1][st-1],dot)
                dotcheck_leftdown=np.char.equal(data[i+1][st-1],dot)
                # dotcheck_rightup=np.char.equal(data[i-1][ed+1],dot)
                # dotcheck_rightdown=np.char.equal(data[i+1][ed+1],dot)
                dotcheck1=np.char.equal(data[i+1][ed],dot)
                dotcheck2=np.char.equal(data[i-1][ed],dot)
                if(st==ed):
                        pass
                else:
                  dotcheckcentreup=np.char.equal(data[i-1][st+1],dot)
                  dotcheckcentredown=np.char.equal(data[i+1][st+1],dot)
                # dotcheckendside=np.char.equal(data[i][ed+1],dot)
                if((numcheck_prev==False and dotcheck_prev==False) or
                    (numcheck_next==False and dotcheck_next==False) or
                      dotcheck_side==False or dotcheck_leftup==False or
                        dotcheck_leftdown==False or

                              dotcheck1==False or
                                dotcheck2==False or
                                  dotcheckcentreup==False or
                                    dotcheckcentredown==False):
                                    print("found a special character"+str(numbers[j]))
                                    output.append(int(numbers[j]))
                                    data[i]=data[i][:st]+('.'*len(numbers[j]))+data[i][(ed+1):]
                                    
                                    
                                    print(data[i])
                else:
                        data[i]=data[i][:st]+('.'*len(numbers[j]))+data[i][(ed+1):]
                        print(data[i])
        
            else:print("nothing matched check code")          
            
    print(str(numbers[j])+" digit finished")


print(data)
numarr=[]
for i in range(len(data)):
    numbers=re.findall(r'\d+',data[i])
    if (numbers==[]):
            pass
    else:
      numarr.append(numbers)

if(numarr==[]):
    print("ALL NUMBERS ARE PROCESSED!!!!")
else:
    print("numbers not processed are")
    print(numarr)
print("PART 1 SOLUTION")
print(sum(output))
end=time.time()
print("Time taken: "+str(end-start)+" seconds")