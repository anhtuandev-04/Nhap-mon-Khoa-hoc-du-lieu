import numpy as np

print("--- BÀI 8: TÌM MAX TRÊN MỖI DÒNG ---")

ma_tran = np.random.randint(0, 10, size=(3, 5))
print("Ma trận 3x5 vừa tạo:\n", ma_tran)

max_tren_dong = np.max(ma_tran, axis=1)

print("\nSố lớn nhất trên từng dòng lần lượt là:")
for i, gia_tri in enumerate(max_tren_dong):
    print(f"- Dòng thứ {i+1}: {gia_tri}")