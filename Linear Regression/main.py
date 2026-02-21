import numpy as np
from mytinyai import LinearRegressor

# 1. Siapkan Data (Latihan)
# X = Berat biji kopi (gram), y = Harga (Rupiah)
# Kita buat data sederhana: 100g=10rb, 200g=20rb, dst.
X_train = np.array([[100], [200], [300], [400], [500]])
y_train = np.array([10000, 20000, 30000, 40000, 50000])

# 2. Inisialisasi Model
# Kita ingin AI belajar 2000 kali dengan kecepatan 0.00001
# (LR kecil karena angka harga sangat besar)
model = LinearRegressor(lr=0.00001, epochs=2000)

# 3. Mulai Latihan (Training)
print("AI sedang mempelajari pola harga...")
model.fit(X_train, y_train)

# 4. Gunakan untuk Prediksi
berat_baru = np.array([[750]]) # Kita tanya: kalau 750 gram harganya berapa?
hasil = model.predict(berat_baru)

print("-" * 30)
print(f"Hasil Prediksi untuk 750g: Rp {hasil[0]:,.0f}")
print(f"Rumus yang ditemukan: Harga = {model.weights[0]:.2f} * Berat + {model.bias:.2f}")