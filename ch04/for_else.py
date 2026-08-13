#「找完所有的東西，如果中途都沒有觸發 break 離開，最後就執行 else。」
ages = [20, 25, 30, 18, 35]

for age in ages:
    if age < 18:
        print("發現未成年人！")
        break  # 🌟 只要觸發了 break，下面的 else 就「絕對不會」執行！
else:
    # 🌟 只有當 for 迴圈把 ages 裡的所有東西都巡過一遍、且都沒觸發 break 時，才會走到這！
    print("檢查完畢，所有人皆已成年。")
    
# 模擬資料庫中的使用者資料
users_db = [
    {"username": "alex", "password": "123"},
    {"username": "bob", "password": "456"},
    {"username": "clara", "password": "789"}
]

input_user = input("請輸入帳號: ")
input_pwd = input("請輸入密碼: ")

for user in users_db:
    if user["username"] == input_user and user["password"] == input_pwd:
        print(f" 歡迎回來，{input_user}！登入成功。")
        break  # 🌟 找到了就跳出，絕對不執行後面的 else
else:
    # 🌟 如果整個資料庫都比對完了（迴圈完整結束），代表沒人匹配成功
    print("❌ 登入失敗：帳號或密碼錯誤。")

# 客人買的水果與倉庫目前的庫存數量
warehouse_stock = {
    "蘋果": 10,
    "香蕉": 5,
    "西瓜": 0,  # 🌟 糟糕，西瓜沒貨了！
    "葡萄": 3
}

for fruit, count in warehouse_stock.items():
    if count == 0:
        print(f"❌ 警告：【{fruit}】已經缺貨！無法完成整筆訂單。")
        break  # 🌟 發現缺貨立刻中斷，不執行 else
else:
    # 🌟 只有當所有水果的庫存都大於 0、安全繞完迴圈時，才會來到這裡
    print(" 檢查完畢！所有商品皆有庫存，開始包裝出貨。")
