#38(1)(2)在主函式中，實現從鍵盤輸入10名學生某門課的成績，儲存在一維陣列中；呼叫排序函式；對排序後的陣列中的元素按從高到低列印輸出。

grades = [] 
i = 0 
for i in range(i, 10): 
    print("the next student's grade is: ")
    x = int(input("")) 
    grades.append(x)

grades.sort(reverse = True)
print(grades) 