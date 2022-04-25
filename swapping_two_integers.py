#40、輸入兩個整數，利用指標變數作為函式引數，程式設計實現兩數互換功能，並將交換後的資料重新輸出。
alist = ["",""] 

alist[0] = int(input(""))
alist[1]= int(input(""))

alist[0], alist[1] = alist[1], alist[0]

print("after the switch, the numbers now are in the order below: \n", alist[0], alist[1])