#使用階乘函式計算n!=1*2*3*(n-l)*n的結果,其中由使用者輸入。n的輸入值必須大於等於1。3


def d(n):
   if n <= 1:
       return 1
   else :            # n > 1        
       return n * d(n-1) 
 
while True:
   n = eval(input('n = '))
   if (n >= 1):
       break
   else:
       print('輸入資料不符, 請重新輸入...')
 
fac = d(n)
print (f'{n}! = {fac}')