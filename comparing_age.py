#從鍵盤輸入你和你朋友的年齡，編成判斷誰的年齡最大，並列印最大者的年齡。

print("enter you and your friend's age: \n")

x_ = input() 
y_ = input()

x = int(x_)
y = int(y_)

import math 
a = max(x ,y) 
print("the one that's older is ")
print(a) 