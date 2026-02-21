import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mytinyai import LinearRegressor

# --- UI Header ---
st.title("🤖 MyTinyAI: Linear Regression dari Nol")
st.write("Aplikasi ini mendemonstrasikan bagaimana AI belajar tanpa API eksternal.")

# --- Sidebar Parameter ---
st.sidebar.header("Konfigurasi Latihan")
lr = st.sidebar.slider("Learning Rate", 0.0001, 0.1, 0.01, format="%.4f")
epochs = st.sidebar.number_input("Jumlah Latihan (Epochs)", 10, 5000, 1000)

# --- Input Data ---
st.subheader("1. Masukkan Data Latihan")
col1, col2 = st.columns(2)
with col1:
    x_input = st.text_area("Data X (pisahkan dengan koma)", "1, 2, 3, 4, 5")
with col2:
    y_input = st.text_area("Data Y (pisahkan dengan koma)", "10, 22, 31, 39, 52")

# Konversi input string ke numpy array
X = np.array([float(i.strip()) for i in x_input.split(",")]).reshape(-1, 1)
y = np.array([float(i.strip()) for i in y_input.split(",")])

# --- Tombol Training ---
if st.button("Mulai Latih AI"):
    model = LinearRegressor(lr=lr, epochs=epochs)
    
    with st.spinner('AI sedang berpikir...'):
        model.fit(X, y)
    
    st.success("Latihan Selesai!")

    # --- Visualisasi Hasil ---
    col_res1, col_res2 = st.columns(2)

    with col_res1:
        st.write("### Grafik Garis Prediksi")
        fig, ax = plt.subplots()
        ax.scatter(X, y, color="red", label="Data Asli")
        ax.plot(X, model.predict(X), color="blue", label="Garis AI")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.legend()
        st.pyplot(fig)

    with col_res2:
        st.write("### Grafik Penurunan Error")
        fig2, ax2 = plt.subplots()
        ax2.plot(range(len(model.loss_history)), model.loss_history)
        ax2.set_xlabel("Iterasi")
        ax2.set_ylabel("Error (Loss)")
        st.pyplot(fig2)

    # --- Fitur Prediksi Baru ---
    st.divider()
    st.subheader("2. Tes Prediksi Data Baru")
    val_baru = st.number_input("Masukkan angka X untuk diprediksi:", value=10.0)
    pred = model.predict(np.array([[val_baru]]))
    st.metric("Hasil Prediksi AI", f"{pred[0]:.2f}")