import streamlit as st
import os

# Set layout halaman
st.set_page_config(page_title="Prediksi Wajah 5 Tahun Lagi", layout="wide")

# Mendapatkan direktori base file ini (app.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

st.title("Prediksi Wajahmu 5 Tahun Lagi Berdasarkan Kebiasaan Belajar")

# Input kebiasaan belajar
habit = st.radio(
    "Seberapa sering kamu belajar dalam seminggu?",
    ("Rajin (5-7 jam)", "Cukup (3-4 jam)", "Freelance (1-2 jam)", "Buruh (kurang dari 1 jam)", "Tukang (tidak belajar)")
)

# Mapping habit ke kata kunci untuk gambar
habit_map = {
    "Rajin (5-7 jam)": "rajin",
    "Cukup (3-4 jam)": "cukup",
    "Freelance (1-2 jam)": "freelance",
    "Buruh (kurang dari 1 jam)": "buruh",
    "Tukang (tidak belajar)": "tukang"
}

key = habit_map[habit]

# Path gambar dengan join path agar aman
img_path = {
    "rajin": os.path.join(BASE_DIR, "images", "dokter.jpg"),
    "cukup": os.path.join(BASE_DIR, "images", "pilot.jpg"),
    "freelance": os.path.join(BASE_DIR, "images", "model.jpg"),
    "buruh": os.path.join(BASE_DIR, "images", "buruh.jpg"),
    "tukang": os.path.join(BASE_DIR, "images", "tukang.jpg")
}

st.write(f"**Prediksi masa depan kamu:** {habit.capitalize()} → Profesi {key.capitalize()}")

# Tampilkan gambar hasil prediksi
image_file = img_path.get(key)
if image_file:
    st.image(image_file, use_column_width=True)
else:
    st.write("Gambar tidak ditemukan.")

