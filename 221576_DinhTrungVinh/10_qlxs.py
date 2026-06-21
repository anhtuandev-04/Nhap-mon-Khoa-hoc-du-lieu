import pandas as pd
import random

df = pd.read_csv(r"C:\Users\HP\Desktop\NhapMonKhoaHocDuLieu\10_Filedulieukqxs.csv")

df["Ngay"] = pd.to_datetime(df["Ngay"], errors="coerce")

df = df.dropna(subset=["So"])
df["So"] = df["So"].astype(int)

df["hai_so_cuoi"] = df["So"] % 100

def choi_chan_le():
    chan = [i for i in range(100) if i % 2 == 0]
    le = [i for i in range(100) if i % 2 == 1]
    if random.choice(["chan","le"]) == "chan":
        return random.sample(chan, 50)
    else:
        return random.sample(le, 50)

print("Chiến lược 1 - Ngẫu nhiên chẵn/lẻ:", choi_chan_le())

def choi_dau_cuoi(chuso=7):
    dau = [chuso*10 + i for i in range(10)]   
    cuoi = [i*10 + chuso for i in range(10)]  
    return sorted(set(dau + cuoi))

print("Chiến lược 2 - Nuôi đầu/cuối số 7:", choi_dau_cuoi(7))

def choi_it_nhat(df):
    freq = df["hai_so_cuoi"].value_counts()
    it_nhat = freq.idxmin()
    return it_nhat, freq[it_nhat]

so_it_nhat, tan_suat = choi_it_nhat(df)
print(f"Chiến lược 3 - Số xuất hiện ít nhất: {so_it_nhat} (xuất hiện {tan_suat} lần)")
