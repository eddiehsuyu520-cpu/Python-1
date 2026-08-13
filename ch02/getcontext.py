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

print(" ── 解決 decimal 運算誤差的正確寫法 ───────────────────")

# ❌ 錯誤寫法（會繼承 float 的二進位誤差）
# d1 = decimal.Decimal.from_float(123.4567)

#  正確寫法：直接傳入字串（String）
d1 = decimal.Decimal('123.4567')
d2 = decimal.Decimal('34.5678')

# 執行相加
result = d1 + d2

print("d1:", d1)
print("d2:", d2)
print("絕對精準的結果 :", result)  # 輸出: 158.0245 (完全沒有任何雜音尾數)

'''在開發 Django 的電商購物車、金流、或是計費系統 時，資料庫傳過來的金額、或者是使用者輸入的數值，在轉成 Decimal 時百分之百要使用字串格式 Decimal('123.45')，絕對不要經過 float 轉手。'''