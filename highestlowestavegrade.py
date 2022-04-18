#44、從鍵盤輸入30名學生的成績資料，求其中的最高分、最低分和平均分。
i, test, test2, sum = 30 , 0 , 101 , 0  
while i > 0: 
    x = input("") 
    grade = int(x) 
    sum = sum + grade 
    if test < grade: 
        test = grade 
    if test2 > grade: 
        test2 = grade 
    i = i - 1 



print ("the average score is: " )
print (sum/30)
print ("the highest score is: ")
print (test)
print ("the lowest score is: ")
print (test2) 
    