star = 10
for x in range(1, star):
    for y in range(1,star-x):
        print(" ", end='')
    for y in range(1, (x*2)):
        print("*", end='')
#        print("*", end=' ')
    print()
print()

'''print() 函式有一個預設的隱形行為：每次印完東西後，它會自動在結尾加上一個換行符號（\n）。
當你寫 end=""（雙引號中間空無一物），就是告訴 Python：「這次印完之後，結尾什麼都不要加，直接停在原地！」'''