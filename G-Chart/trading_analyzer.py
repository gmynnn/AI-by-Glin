import streamlit as st
import google.generativeai as genai
from PIL import Image
import io

st.set_page_config(
    page_title="G-Chart - AI Trading Analyzer",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<div style='text-align: center; padding: 20px 0;'>
    <h1 style='color: #1f77b4; font-size: 3em; margin-bottom: 0;'>📊 G-Chart</h1>
    <p style='font-size: 1.2em; color: #666; margin-top: 10px;'>
        Artificial Intelligence Trading Chart Analyzer
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
            padding: 20px; border-radius: 10px; margin-bottom: 30px; color: white;'>
    <p style='font-size: 1.1em; margin: 0; text-align: center;'>
        🎯 <strong>G-Chart</strong> adalah AI assistant profesional yang menganalisis chart trading Anda 
        menggunakan berbagai metode analisis teknikal populer untuk memberikan insight mendalam 
        tentang level-level kritis, momentum pasar, dan rekomendasi trading yang objektif.
    </p>
</div>
""", unsafe_allow_html=True)

GEMINI_API_KEY = "AIzaSyCMvW74vTiJiJgetKjIxOPj3Bor2j3WT78"

api_key = GEMINI_API_KEY

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📤 Upload & Konfigurasi")
    
    uploaded_file = st.file_uploader(
        "Pilih gambar chart (PNG/JPG)",
        type=["png", "jpg", "jpeg"],
        help="Upload screenshot chart trading Anda"
    )
    
    analysis_type = st.selectbox(
        "Pilih Teknik Analisis:",
        [
            "Support & Resistance (SNR)", 
            "Supply & Demand (SND)", 
            "Elliott Wave Theory", 
            "Harmonic Patterns", 
            "Price Action Analysis",
            "Indikator (RSI, MACD, Moving Average)"
        ],
        help="Pilih metode utama yang ingin digunakan AI untuk menganalisis chart"
    )

    rr_ratio = st.number_input(
        "Target Risk/Reward Ratio (1:X):", 
        min_value=1.0, 
        max_value=20.0, 
        value=2.0, 
        step=0.5,
        help="Tentukan berapa target keuntungan dibandingkan dengan risiko Anda"
    )
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Preview Chart", use_container_width=True)
        
        analyze_button = st.button("🔍 Analisis Chart", type="primary", use_container_width=True)
    else:
        analyze_button = False
        st.info("👆 Upload gambar chart terlebih dahulu")

with col2:
    st.subheader("📊 Hasil Analisis")
    
    if analyze_button:
        if not api_key:
            st.error("❌ API Key tidak ditemukan!")
        else:
            try:
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel('gemini-2.5-flash')
                
                with st.spinner(f"🤖 G-Chart AI sedang menganalisis menggunakan metode {analysis_type}..."):
                    img_byte_arr = io.BytesIO()
                    image.save(img_byte_arr, format=image.format if image.format else 'PNG')
                    img_byte_arr.seek(0)
                    
                    prompt = f"""
Anda adalah G-Chart, seorang AI Trading Analyst profesional.

Analisis gambar chart trading ini secara mendalam menggunakan teknik utama: {analysis_type}.
Pastikan manajemen risiko yang Anda berikan mengacu pada target Risk/Reward Ratio minimal 1:{rr_ratio}.

Tugas Anda:
1. Identifikasi elemen kunci berdasarkan teknik {analysis_type} (misal: area SND, gelombang Elliott, atau pola Harmonic).
2. Analisis struktur pasar dan momentum saat ini.
3. Berikan rekomendasi posisi yang paling logis.

Format jawaban Anda:

**HASIL ANALISIS TEKNIKAL ({analysis_type.upper()})**

📍 **Key Levels & Structure:**
[Jelaskan level-level penting atau struktur yang ditemukan]

📈 **Market Sentiment:**
[Jelaskan kondisi market berdasarkan teknik yang dipilih]

💡 **STRATEGI TRADING: [BUY/SELL/WAIT]**

**Rencana Eksekusi:**
- Entry Point: [Harga]
- Stop Loss: [Harga]
- Take Profit: [Harga] (Dihitung berdasarkan Target RR 1:{rr_ratio})
- Aktual Risk/Reward Ratio: 1:[Sebutkan ratio yang Anda buat]

**Alasan Logis:**
[Jelaskan mengapa Anda merekomendasikan hal tersebut]

**Catatan Tambahan:**
[Tips atau peringatan terkait volatilitas atau konfirmasi candle berikutnya]

Berikan analisis yang objektif. Gunakan Bahasa Indonesia yang profesional.
"""
                    
                    response = model.generate_content([prompt, image])
                    
                    st.markdown("### ✅ Analisis G-Chart Selesai")
                    st.markdown(response.text)
                    
                    st.markdown("---")
                    st.warning("""
                    ⚠️ **DISCLAIMER G-CHART:** Analisis ini dihasilkan oleh G-Chart AI untuk tujuan edukasi. Keputusan trading sepenuhnya menjadi tanggung jawab Anda.
                    """)
                    
            except Exception as e:
                st.error(f"❌ Terjadi kesalahan: {str(e)}")
    else:
        st.info("👈 Konfigurasi analisis dan klik tombol 'Analisis' untuk memulai")

st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666; padding: 20px;'>
        <p style='font-size: 1.1em;'><strong>G-Chart</strong> - AI-Powered Trading Chart Analyzer</p>
    </div>
    """,
    unsafe_allow_html=True
)