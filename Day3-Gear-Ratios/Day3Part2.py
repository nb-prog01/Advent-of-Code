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
data=np.loadtxt ('Gear.txt',dtype='object',comments=None)
data=np.array(data)
temp_data=[]
print(len(data))
num_indices=[]

dot=np.array('*')
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

                if( dotcheck==True or dotcheckcentredown==True or dotcheck_side==True or dotcheck_leftdown==True or dotcheck_rightdown==True or dotcheckendside==True or dotcheck1==True):
                    print("found a gear character attached to: "+str(numbers[j]))
                    output.append({(numbers[j]),(st,ed)})
                    for nums_i in list(range(st,ed+1)):
                        num_indices.append((i,nums_i))
                    
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
                if((numcheck_prev==False and dotcheck_prev==True) or
                    (numcheck_next==False and dotcheck_next==True) or
                      dotcheck_side==True or dotcheck_leftup==True or
                        dotcheck_leftdown==True or
                          dotcheck_rightup==True or
                            dotcheck_rightdown==True or
                              dotcheck1==True or
                                dotcheck2==True or
                                  dotcheckcentreup==True or
                                    dotcheckcentredown==True or
                                    dotcheckendside==True):
                                    print("found a special character"+str(numbers[j]))
                                    output.append({(numbers[j]),(st,ed)})
                                    for nums_i in list(range(st,ed+1)):
                                          num_indices.append((i,nums_i))
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

                if((numcheck_prev==False and dotcheck_prev==True) or
                    
                      dotcheck_side==True or
                        dotcheck_leftup==True or
                        
                          dotcheck_rightup==True or
                            
                              
                                dotcheck2==True or
                                  dotcheckcentreup==True or
                                    
                                    dotcheckendside==True):
                                    print("found a special character"+str(numbers[j]))
                                    output.append({(numbers[j]),(st,ed)})
                                    for nums_i in list(range(st,ed+1)):
                                          num_indices.append((i,nums_i))
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

                if((numcheck==False and dotcheck==True) or dotcheck_rightdown==True or dotcheckendside==True or dotcheck1==True):
                    print("found a special character"+str(numbers[j]))
                    output.append({(numbers[j]),(st,ed)})
                    for nums_i in list(range(st,ed+1)):
                        num_indices.append((i,nums_i))
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

                if((numcheck_prev==False and dotcheck_prev==True) or
                        
                          dotcheck_rightup==True or
                            
                              
                                dotcheck2==True or
                                  dotcheckcentreup==True or
                                    
                                    dotcheckendside==True):
                                    print("found a special character"+str(numbers[j]))
                                    output.append({(numbers[j]),(st,ed)})
                                    for nums_i in list(range(st,ed+1)):
                                          num_indices.append((i,nums_i))

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
                if((numcheck_prev==False and dotcheck_prev==True) or
                    (numcheck_next==False and dotcheck_next==True) or
                      
                        
                          dotcheck_rightup==True or
                            dotcheck_rightdown==True or
                              dotcheck1==True or
                                dotcheck2==True or
                                  dotcheckcentreup==True or
                                    dotcheckcentredown==True or
                                    dotcheckendside==True):
                                    print("found a special character"+str(numbers[j]))
                                    output.append({(numbers[j]),(st,ed)})
                                    for nums_i in list(range(st,ed+1)):
                                          num_indices.append((i,nums_i))
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

                if((numcheck==False and dotcheck==True) or dotcheck_side==True or dotcheck_leftdown==True or dotcheck1==True):
                    print("found a special character"+str(numbers[j]))
                    output.append({(numbers[j]),(st,ed)})
                    for nums_i in list(range(st,ed+1)):
                        num_indices.append((i,nums_i))
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

                if((numcheck_prev==False and dotcheck_prev==True) or
                    
                      dotcheck_side==True or
                        dotcheck_leftup==True or
                        
                          
                            
                              
                                dotcheck2==True or
                                  dotcheckcentreup==True
                                    
                                    ):
                                    print("found a special character"+str(numbers[j]))
                                    output.append({(numbers[j]),(st,ed)})
                                    for nums_i in list(range(st,ed+1)):
                                          num_indices.append((i,nums_i))
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
                if((numcheck_prev==True and dotcheck_prev==True) or
                    (numcheck_next==True and dotcheck_next==True) or
                      dotcheck_side==True or dotcheck_leftup==True or
                        dotcheck_leftdown==True or

                              dotcheck1==True or
                                dotcheck2==True or
                                  dotcheckcentreup==True or
                                    dotcheckcentredown==True):
                                    print("found a special character"+str(numbers[j]))
                                    output.append({(numbers[j]),(st,ed)})
                                    for nums_i in list(range(st,ed+1)):
                                          num_indices.append((i,nums_i))
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
print(output)
print(output[0])
print(num_indices)
end=time.time()
print("Time taken: "+str(end-start)+" seconds")