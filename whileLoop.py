"""
计算 0 ~ 100 之间所有数字的累计求和结果
"""
# i = 1
# sum_num = 0
# while i <= 100:
#     sum_num = sum_num + i
#     i += 1
# print("0-100的累计求和:%d" % sum_num)
"""
计算 0 ~ 100 之间 所有 偶数 的累计求和结果
"""
# i = 0
# sum_num = 0
# while i <= 100:
#     if i % 2 == 0:
#         sum_num = sum_num + i
#     i += 1
# print("0-100的累计求和:%d" % sum_num)
# i = 0
# while i < 5:
#     if i == 4:
#         break
#     print(i)
#     i += 1
# print("over")
# i = 0
# while i < 5:
#     if i == 4:
#         i += 1  # 严防死循环
#         continue
#     print(i)
#     i += 1
# print("over")
# 九九乘法表
# row = 1
# while row <= 9:
#     col = 1
#     while col <= row:
#         print("%d + %d = %d" %(col, row, (col * row)), end="\t")
#         col += 1
#     print()  #while防止死循环
#     row += 1