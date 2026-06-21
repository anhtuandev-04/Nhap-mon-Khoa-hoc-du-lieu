import numpy as np

print("--- THAY THẾ PHẦN TỬ LẺ BẰNG SỐ -1 ---")

mang_20 = np.random.randint(1, 50, size=20)
print("Mảng ban đầu khi chưa sửa đổi:\n", mang_20)

mang_20[mang_20 % 2 != 0] = -1

print("\nMảng sau khi đã biến đổi toàn bộ số lẻ thành -1:\n", mang_20)