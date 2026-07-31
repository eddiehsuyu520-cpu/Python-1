print("1.蘋果\n2.香蕉\n3.芒果\n")
print(" ")
option = int(input("請輸入選項<1~3>："))
if option == 1:
    print("英文單字： apple")
elif option == 2:
    print("英文單字： banana")
elif option == 3:
    print("英文單字： mango")
else:
    print("輸入錯誤!")
    
'''編寫程式，輸入一個1~12之間的整數，輸入3、4、5時，顯示「春天」；輸入6、7、8時，顯示「夏天」；輸入9、10、11時，顯示「秋天」；當輸入12、1、2時，顯示「冬天」。輸入其它數字，顯示「輸入錯誤！」。'''
# EXAMPLE:請輸入一個 1~12 之間的月份： 6   
# 6月是夏天

month = int(input("請輸入一個 1~12 之間的月份： "))
if month in [3, 4, 5]:
    print(f"{month}月是春天")
elif month in [6, 7, 8]:
    print(f"{month}月是夏天")
elif month in [9, 10, 11]:
    print(f"{month}月是秋天")
elif month in [12, 1, 2]:
    print(f"{month}月是冬天")
else:
    print("輸入錯誤！")

'''請以if … else if … 的結構，撰寫一個程式依年收入多寡繳納不同稅率之稅額。
54萬元以下免稅，大於54萬至121萬稅率12%，大於121萬至242萬稅率20%，
大於242萬至453萬稅率30%，大於453萬至1031萬稅率40%，大於1031萬以上稅率45%，'''    
income = int(input("請輸入您的綜合所得淨額："))
if income < 540000:
     tax = 0
elif income < 1210000:
     tax = income*0.12
elif income < 2420000:
		 tax = income*0.2
elif(income < 4530000):
		 tax = income*0.3
elif(income < 10310000):
		 tax = income*0.4
else:
     tax = income*0.45
print(f"您所要繳交的所得稅額是：{tax:.1f}")