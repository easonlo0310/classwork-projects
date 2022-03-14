#有一函式當x< 0 時 y=1，當 x>0 時，y=3，當 x=0 時 y=5，程式設計，從鍵盤輸入一個x值，輸出y值。

print ("insert an x value for the function y")
s = input() 
x = float(s)
y = 0 
if x < 0: 
    y = 1 
elif x > 0: 
    y = 3 
elif x == 0: 
    y = 5 
    
print ("the value is ", y) 