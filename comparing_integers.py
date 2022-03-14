#編寫一個程式,從4個整數中找出最小的數,並顯示此數 

print("insert the four numbers you wish to compare: ")
a = input ()
b = input ()
c = input ()
d = input ()

alist = list((a, b,c, d))
alist.sort()  
print ("the smallest integer is ")
print (alist[0]) 