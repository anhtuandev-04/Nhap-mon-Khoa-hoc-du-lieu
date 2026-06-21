import numpy as np

print("--- BÀI 9: TÍNH KHOẢNG CÁCH EUCLID ---")

a = np.random.randint(1, 10, 10)
b = np.random.randint(1, 10, 10)

print("Mảng a:", a)
print("Mảng b:", b)

khoang_cach_1 = np.sqrt(np.sum((a - b) ** 2))

khoang_cach_2 = np.linalg.norm(a - b)

print("\nKết quả khoảng cách Euclid:")
print("- Tính theo công thức thủ công :", khoang_cach_1)
print("- Tính bằng hàm chuyên gia     :", khoang_cach_2)