flavor = "0123456789abcde"
print(flavor[0:3])
print(flavor[3:7])
print(flavor[3:])
print(flavor[:])
print(flavor[:14])
print(flavor[13:15])
print(flavor[19:20])  #超出範圍=>不顯示
print(flavor[-7:-4])
print(flavor[-7:0])
print(flavor[-7:])
print(flavor[-3:])

print(flavor[-1]) #代表最後一個字元。
print(flavor[::2]) #從頭到尾，每隔 2 個字取一次。
print(flavor[::-1]) #步長為 -1 代表倒著走，能直接把字串顛倒過來。
