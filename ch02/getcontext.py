import decimal           # 匯入 decimal 模組
d1=decimal.Decimal.from_float(123.4567)
d2=decimal.Decimal.from_float(34.5678)
print(decimal.getcontext())
print(decimal.getcontext().prec)        # ⇨ 28
print(decimal.getcontext().rounding)    # ⇨ ROUND_HALF_EVEN
#把 123.4567當成數字直接放進括號時，Python 就已經當作一般的二進位浮點數（float）處理了。硬體此時就已經產生了微小的二進位誤差。
print(d1+d2)         # ⇨ 158.0244999999999619140909363
# 設定小數位數,以便四捨五入後排除硬體轉換的誤差。
decimal.getcontext().prec=8
print(d1+d2)         # ⇨ 158.02450