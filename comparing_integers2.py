#從鍵盤輸入兩個數，求出其最大值（要求使用函式完成求最大值，並在主函式中呼叫該函式）
print ("enter two numbers to you wish to compare: \n") 
x_ = input() 
y_ = input()

x = int(x_)
y = int(y_)

alist = [x, y] 
alist.sort() 
print("the larger number is: ") 
print (alist[1])