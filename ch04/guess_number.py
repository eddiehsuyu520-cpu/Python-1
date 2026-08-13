number = 7
chance = 5
i = 0
for i in range(chance):
    guess = int(input(f"請猜一個數字（剩餘 {chance - i} 次機會）: "))
    if guess == number:
        print("🎉 恭喜你，猜對了！")
        break  # 🌟 猜對了就 break 跳出，不會執行 else
    elif guess < number:
        print("你猜的數字太小了！")
    else:
        print("你猜的數字太大了！")
else:
    # 🌟 只有當 chance 變成 0，for 條件 (0 > 0) 不成立自然結束時，才會走到這
    print(f"❌ 遺憾，機會用盡！正確答案是 {number}。")