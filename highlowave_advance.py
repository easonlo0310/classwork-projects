#45、從鍵盤輸入某班學生某門課的成績及其學號（班級人數最多40人，具體人數由鍵盤輸入），輸出該班最高分和最低分及其學生學號；並輸出該班該課程的總分和平均分。請編寫程式。

i, test, test2, sum = 30 , 0 , 101 , 0  
highest = 0 
lowest = 0 
while i > 0: 
    x = input("input the grade: \n") 
    grade = int(x) 
    sum = sum + grade 

    y = input("input your student's number: \n")
    if test < grade: 
        test = grade
        highest = y  
    if test2 > grade: 
        test2 = grade 
        lowest = y 
    i = i - 1 

print ("highest score is: ", test, ",the student number is: " , highest) 
print ("lowest score is : ", test, ",the student number is: " , lowest) 
print ("the sum is : ", sum )
print ("the average is: ", sum/30)