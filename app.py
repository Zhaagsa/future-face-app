import streamlit as st
from PIL import Image
import random

def predict_future(hours_per_week):
    if hours_per_week < 1:
        return "Buruh", "images/buruh.jpg"
    elif hours_per_week < 3:
        return "Tukang", "images/tukang.jpg"
    elif hours_per_week < 5:
        return "Freelancer", "images/freelancer.jpg"
    else:
        professions = [("Dokter", "images/dokter.jpg"),
                       ("Pilot", "images/pilot.jpg"),
                       ("Model", "images/model.jpg")]
        return random.choice(professions)

st.title("📸 Prediksi Wajahmu 5 Tahun Lagi Berdasarkan Kebiasaan Belajar")

uploaded_file = st.file_uploader("Upload foto wajah kamu (jpg/png)", type=["jpg", "jpeg", "png"])
hours = st.slider("Jam belajar per minggu:", 0.0, 10.0, 1.0)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Foto Kamu Sekarang", use_column_width=True)

    if st.button("Lihat Wajahmu 5 Tahun Lagi"):
        profesi, future_path = predict_future(hours)
        st.success(f"Berdasarkan kebiasaan belajarmu, kamu akan jadi: **{profesi}**")
        future_img = Image.open(future_path)
        st.image(future_img, caption="Prediksi Masa Depan", use_column_width=True)