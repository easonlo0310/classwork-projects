#42. 輸入一數字，請將此數字的所有位數，作所有位數的加總 

def split(num): 
    return list(num)

num = input("") 
i = len(num) - 1 
x = 0 
while i > 0: 
    x = int(num[i]) + x 
    i = i - 1     
print (x)