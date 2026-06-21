import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

df = pd.read_csv(r"C:\Users\HP\Desktop\NhapMonKhoaHocDuLieu\wine-quality\winequality-red.csv", sep=";")

print("5 dòng đầu tiên:")
print(df.head())
print("\nThông tin dữ liệu:")
print(df.info())

corr_alcohol_quality = df["alcohol"].corr(df["quality"])
print(f"\nTương quan giữa alcohol và quality: {corr_alcohol_quality:.3f}")

plt.scatter(df["alcohol"], df["quality"], alpha=0.5)
plt.xlabel("Alcohol")
plt.ylabel("Quality")
plt.title("Mối quan hệ giữa Alcohol và Quality")
plt.show()

corr_all = df.corr()["quality"].sort_values(ascending=False)
print("\nTương quan giữa các thuộc tính với quality:")
print(corr_all)

features = ["alcohol", "volatile acidity", "sulphates"]
X = df[features]
y = df["quality"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("\nHệ số hồi quy:", model.coef_)
print("Sai số R^2:", r2_score(y_test, y_pred))

plt.scatter(y_test, y_pred, alpha=0.5)
plt.xlabel("Quality thực tế")
plt.ylabel("Quality dự đoán")
plt.title("So sánh giá trị thực tế và dự đoán")
plt.show()
