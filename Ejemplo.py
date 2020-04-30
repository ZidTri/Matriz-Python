n=3
i=0
j=-1
k=1
h=1
p=1
matriz = [[1,2,3],[4,5,6],[7,8,9]]
while n>=0:
    if k==1:
        if h==1:
            for t in range (n):
                j = j+1
                print (matriz[i][j], end='')
            h = h+1
        else: 
            for t in range (n):
                j = j-1
                print (matriz[i][j], end='')
                
            h = h-1
        n=n-1
        k=k+1
    else:
        if p==1:
            for t in range (n):
                i = i+1
                print (matriz[i][j], end='')
                
            p= p+1
        else: 
            for t in range (n):
                i = i-1
                print (matriz[i][j], end='')
                
            p= p-1
        k=k-1