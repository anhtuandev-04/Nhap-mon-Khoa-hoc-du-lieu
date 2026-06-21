import numpy as np

print("--- GHÉP NGANG HAI MẢNG CÓ CÙNG SỐ DÒNG (HSTACK) ---")

a = np.array([[1, 2], 
              [3, 4]])

b = np.array([[5, 6, 7], 
              [8, 9, 10]])

print("Mảng a:\n", a)
print("Mảng b:\n", b)

c = np.hstack((a, b))

print("\nMảng c sau khi ghép ngang (Cột của a xếp trước, cột của b nối sau):\n", c)
print("Cấu trúc mảng c hiện tại là:", c.shape)