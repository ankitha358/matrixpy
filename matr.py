m=int(input('Enter no. of rows:'))
n=int(input('Enter no. of columns:'))

mat = [[0 for x in range(n)] for y in range(m)]
mat[0][0]=1
mat[m-1][n-1]=n*m
imax=0
jmax=0
i=1
j=0

for count in range(2,(m*n)):
    if(i>imax):
        imax=i
    if(j>jmax):
        jmax=j
    mat[i][j]=count
    if(i==0 or j==n-1):
        if(imax>=m-1):
            i=m-1
        else:
            i=imax+1
        for col in range(n):
            if(mat[i][col]==0):
                j=col
                break
    elif(i!=0):
        j+=1
        i-=1
    elif(i==j):
        j+=1
        i-=1


for i in mat:
    for j in i:
        print(j,end=' ')
    print('')