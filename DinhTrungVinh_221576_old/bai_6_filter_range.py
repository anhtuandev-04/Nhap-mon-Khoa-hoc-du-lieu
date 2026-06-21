import numpy as np

print("--- BÀI 6: LỌC PHẦN TỬ TRONG KHOẢNG 5 ĐẾN 10 ---")

a = np.random.randint(0, 20, 20)
print("Mảng a ban đầu:\n", a)

ket_qua = a[(a >= 5) & (a <= 10)]

print("\nCác phần tử nằm trong khoảng [5, 10]:\n", ket_qua)