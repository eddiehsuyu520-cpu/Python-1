print("===主功能表===\n1.新增作業\n2.修改作業\n3.查詢作業\n0.結束程式")
number = int(input("請輸入選項(0~3): "))
while number ==1:
    print("新增作業")
    break
while number ==2:
    print("修改作業")
    break
while number ==3:
    print("查詢作業")
    break
while number ==0:
    print("結束程式")
    break 
while number not in [0, 1, 2, 3]:
    print("輸入值不正確")
    break


for x in range(1,6):
    for y in range(6,x,-1):
        print(" ",end="")
    for y in range(x,0,-1):
        print(f"{y}", end="")
    print()