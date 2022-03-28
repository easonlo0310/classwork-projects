#10. 從鍵盤輸入10個整數，統計其中正數、負數和零的個數，並在螢幕上輸出。
i = 0 
positive, negative, zeros = 0, 0, 0
while i < 10: 
    y = input("input a number: ")
    x = int(y)
    if x > 0: 
        positive += 1 
    elif x < 0: 
        negative += 1 
    elif x == 0: 
        zeros += 1 
    i += 1 

print ("the number of positive numbers inputed are: ")
print (positive)
print ("the number of positive numbers inputed are: ")
print (negative)
print ("the number of zeros inputed are: ")
print (zeros)