Data = [['老張', '0911443300'], ['Mary', '0928000001'],
         ['發叔', '0431748484'], ['Tom', '0912345678'],
         ['李董', '0255111111'], ['豪哥', '0977229900'], 
         ['小何', '0928888888']] 
query = input("輸入查詢的姓名：")
for i in range(len(Data)):
    if query == Data[i][0]:
        print(f"{Data[i][0]}的電話是{Data[i][1]}")
        break
else:
    print(f"查無 {query} 的資料")


select = int(input("1. 由小到大排序   2. 由大到小排序 :"))
name = ['老張', '發叔', '李董', '豪哥', '小何']
age= [54, 46, 50, 40, 38]
for i in range(len(age)-1):
    for j in range(len(age)-1-i):
            if age[j] > age[j+1]:
                age[j], age[j+1] = age[j+1], age[j]
                name[j], name[j+1] = name[j+1], name[j]            
if select == 1:
  print("由小到大排序:",end="")
  for i in range(len(age)):
    print(f" {name[i]}:{age[i]}",end=" ")              
elif select == 2:
  print("由大到小排序:",end="")
  #name.reverse()
  #age.reverse()
  for i in range(len(age)):
    print(f" {name[len(age)-1-i]}:{age[len(age)-1-i]}",end=" ")
else:
  print("輸入錯誤")


print("\n")

A=[[(x+1)*(y+1)for x in range(9)] for y in range(9)]
for i in range(9):
    for j in range(9):
        print(f"{A[i][j]:2d}", end=" ")
    print()
