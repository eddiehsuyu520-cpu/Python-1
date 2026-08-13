import random as R
# 生成 5 個 1 到 10 之間的隨機整數
for i in range(5):
    # 生成隨機整數
    rnd = R.randint(1, 10)
    # 輸出結果
    print(f'第 {i+1} 個亂數 : {rnd}')