import numpy as np

print("--- BÀI 7: TẠO 1000 SỐ THỰC TỪ -0.5 ĐẾN < 0.5 ---")

arr_float = np.random.uniform(-0.5, 0.5, 1000)

print(f"Đã tạo thành công mảng gồm {len(arr_float)} phần tử!")
print("In thử 10 phần tử đầu tiên để kiểm tra:")
print(arr_float[:10])