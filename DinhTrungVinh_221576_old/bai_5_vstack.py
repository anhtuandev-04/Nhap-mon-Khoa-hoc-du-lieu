import numpy as np

print("--- GHÉP DỌC HAI MẢNG CÓ CÙNG SỐ CỘT (VSTACK) ---")

x = np.array([[1, 2, 3], 
              [4, 5, 6]])

y = np.array([[7, 8, 9]])

print("Mảng x:\n", x)
print("Mảng y:\n", y)

z = np.vstack((x, y))

print("\nMảng z sau khi ghép dọc (Dòng của x ở trên, dòng của y ở dưới):\n", z)
print("Cấu trúc mảng z hiện tại là:", z.shape) 