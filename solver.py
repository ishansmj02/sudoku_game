#--------------------------------------------------------------------------------
def ifpossible(x,y,n):
    for i in range(size):
        if(arr[x][i]==n):
            return 0
    for i in range(size):
        if(arr[i][y]==n):
            return 0
    i=int(x/sz)*sz
    j=int(y/sz)*sz
    k=i+sz
    l=j+sz
    while i<k:
        j=int(y/sz)*sz
        while j<l:
            if arr[i][j]==n:
                return 0
            j=j+1
        i=i+1
    return 1
#--------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def rec(r,c):
    f_c=0
    while r<rows:
        if f_c==1:
            c=0
        while c<cols:
            if arr[r][c]==0:
                f=0
                for i in range(size):
                    if ifpossible(r,c,i+1)==1:
                        f=1
                        arr[r][c]=i+1
                        if c+1==cols:
                            next_c=0
                            next_r=r+1
                        else:
                            next_c=c+1
                            next_r=r
                        if next_r==rows:
                            return 1
                        if rec(next_r,next_c)==1:
                            return 1
                        else:
                            f=0
                if f==0:
                    arr[r][c]=0
                    return 0
            c=c+1
            if c==cols:
                f_c=1
        r=r+1
    return 1
#----------------------------------------------------------------------------
sz=3
size=sz*sz
rows=size
cols=size
arr=[[0 for i in range(cols)] for j in range(rows)]

arr=[[0,7,9,0,4,0,0,0,0],
     [0,1,8,0,0,0,0,0,0],
     [0,0,0,0,0,8,0,0,2],
     [8,0,0,4,0,5,0,0,0],
     [0,4,0,0,9,0,0,6,0],
     [0,0,0,2,0,6,4,0,1],
     [5,0,0,3,0,0,0,0,0],
     [0,0,0,0,0,0,0,9,0],
     [0,0,0,0,6,0,7,4,0]]

import time
start_time = time.time()
rec(0,0)
#print(arr)
for i in range(size):
    print(arr[i])
print("---%s sec---"%(time.time()-start_time))


print("1st commit to sami")



