yesNo = 'y'
pssScore, maxScore, minScore = 85,100,0
power1 = power2 = 100
total = 1.23456e+6
print(yesNo)
print(pssScore, maxScore, minScore)
print(power1, power2)
print(total)
del total
#print(total)  #刪除 total 變數後，會出現 NameError: name 'total' is not defined
print(type(12))       # 顯示整數常值 12 的類別        ⇨ <class 'int'>
print(bin(12))        # 顯示整數常值 12 的二進制值     ⇨ 0b1100
print(oct(12))        # 顯示整數常值 12 的八進制值     ⇨ 0o14
print(hex(12))        # 顯示整數常值 12 的十六進制值   ⇨ 0xc
print('12'*4)         # 顯示 '12'*4 的結果           ⇨ 12121212
print(type('12'))     # 顯示 '12' 的類別             ⇨ <class 'str'>
print(int('12')*4)    # 顯示 int('12')*4 的結果      ⇨ 48