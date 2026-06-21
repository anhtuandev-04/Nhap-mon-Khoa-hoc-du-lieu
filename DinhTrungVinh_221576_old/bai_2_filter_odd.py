import numpy as np

print("--- TÁCH CÁC PHẦN TỬ LẺ TỪ MẢNG 100 PHẦN TỬ ---")

mang_goc = np.random.randint(0, 500, size=100)
print("1. Mảng gốc ban đầu (100 phần tử):\n", mang_goc)

mang_le = mang_goc[mang_goc % 2 != 0]

print("\n2. Mảng sau khi lọc chỉ còn các số lẻ:")
print(mang_le)
print(f"\n=> Đã lọc được {len(mang_le)} số lẻ từ 100 phần tử ban đầu!")