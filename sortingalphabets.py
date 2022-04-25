#39、程式設計實現如下功能：從鍵盤輸入一行字元，統計其中大寫英文字元，小寫英文字元和其他字元的個數。

def split(word):
    return list(word)

word = input("Enter a word: ")

i = 0 
low, cap = 0, 0 
while i < len(split(word)):
    check = split(word)[i].islower() 
    if check == True: 
        low += 1 
    else:
        cap += 1 
    i += 1 

print ("the number of capitalized letters are: ", cap)
print ("the number of lower cased letteres are: ", low)