import math;

radius = 5.0;
circle_area = math.pi * pow(radius, 2);
print(f"The area of the circle is: {circle_area:.2f}");

# This line will raise an error because circle_area is a float, not a string or list.
# print(f"The area of the circle is: {circle_area[:.2f]}");  


# Python內建函數 hex() 轉出來的結果是字串（字元）
r, g, b = 255, 165, 0 # 橘色 
hex_color = f"#{hex(r)[2:]}{hex(g)[2:]}{hex(b)[2:]}"
# # 0xff 0xa5 0x0  ff a5 0  #ffa50
print(hex_color) # 輸出：#ffa50
