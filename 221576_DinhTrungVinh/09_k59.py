import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\HP\Desktop\NhapMonKhoaHocDuLieu\09_Filedulieuk59.csv")

print("Toàn bộ dữ liệu:")
print(df)

print("\n5 dòng đầu tiên:")
print(df.head(5))

print("\n5 dòng cuối cùng:")
print(df.tail(5))

gioi = df[df["Diem"] >= 8]
print(f"\nSố bạn đạt loại giỏi (>=8): {len(gioi)}")

truot = df[(df["Diem"] < 4) | (df["Diem"].isna())]
print(f"Số bạn trượt môn (<4 hoặc không có điểm): {len(truot)}")

plt.figure(figsize=(8,6))
plt.hist(df["Diem"].dropna(), bins=10, range=(1,10), edgecolor="black", color="skyblue")
plt.title("Phân bố điểm số lớp K59")
plt.xlabel("Điểm số")
plt.ylabel("Số lượng sinh viên")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()
