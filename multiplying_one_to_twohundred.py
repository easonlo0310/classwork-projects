#11、程式設計序實現求1-200之間的所有數的乘積並輸出

#direct calculation of the result 
i = 0 
z = 1
x = 1
while i < 200:   
    z = x * z 
    i += 1 
    x += 1 
print (z) 

#use of recursion 
def recursion(k): 
    if k > 0: 
        result = k * recursion(k-1)
        print(result)
    else: 
        result = 1  
    return result 

recursion (200)