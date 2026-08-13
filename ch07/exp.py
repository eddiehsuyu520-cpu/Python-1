import math
principal = 10000 # 本金 10,000
rate = 0.05 # 年利率 5%
years = 3 # 3 年
# 計算連續複利公式：A = P * e^(r*t)
amount = principal * math.exp(rate * years)
print(f"連續複利後的總金額：{amount:.2f}")
# 連續複利後的總金額：11618.34
amount1 = principal * pow((1 + rate), years)
print(f"連續複利後的總金額：{amount1:.2f}")

'''連續複利計息的頻率是「無限次」,所以賺取的利息會比一年只計息一次的年複利還要。
   年複利(Annual Compounding):一年只結算並滾入一次利息。
   連續複利(Continuous Compounding)：利息在每一秒、甚至每個極小瞬間都在不斷滾入本金計算下一次利息。'''