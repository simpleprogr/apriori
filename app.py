import pandas as pd
import streamlit as st
from PIL import Image
from komputasi import data_summary, MBA

# Set judul dan ikon
st.set_page_config(page_title="Underprice Skincare", page_icon="images/icon.jpg", layout="wide")

# Menampilkan judul dan deskripsi
st.markdown("<h1 style='text-align: center; color: black; background: url('http://i49.tinypic.com/2zs1z79.png') 0 0 repeat-x;'>Implementasi Data Mining Untuk Menentukan Pola Penjualan Produk Kecantikan Menggunakan Algoritma Apriori</h1>", unsafe_allow_html=True)
#st.title('Underprice Skincare')
#st.write('Implementasi Data Mining Dalam Menganalisis Pola Penjualan Produk Kecantikan Menggunakan Metode Algoritma Apriori')

# Menampilkan gambar
image = Image.open('images/icon.jpg')
col1, col2, col3 = st.beta_columns([1,2,1])

with col1:
    st.write(' ')

with col2:
    st.write(' ')
    st.image(image)

with col3:
    st.write(' ')
#st.image(image)

# Memuat dataset
dataset_file = st.file_uploader("Upload Dataset Penjualan (.csv)", type=['csv'])
st.write('Contoh format dataset : ')
st.write('- Kode,Date,Item')
st.write('- [Download Contoh Dataset Disini](https://www.kaggle.com/datasets/heeraldedhia/groceries-dataset?datasetId=877335&sortBy=voteCount)')

# Menangani kesalahan saat memuat dataset
if dataset_file is None:
    st.warning('Mohon upload dataset Anda!')
    st.stop()

try:
    df = pd.read_csv(dataset_file)
except Exception as e:
    st.error(f"Terjadi kesalahan saat membaca file: {str(e)}")
    st.stop()

# Mendapatkan nama kolom
if df is not None and not df.empty:
    try:
        pembeli, tanggal, produk = df.columns[0], df.columns[1], df.columns[2]

        # Memanggil fungsi untuk prapemrosesan data
        df = data_summary(df, pembeli, tanggal, produk)

        # Memanggil fungsi untuk melakukan Association Rule Mining menggunakan Apriori
        MBA(df, pembeli, produk)
    except IndexError:
        st.warning("Indeks di luar batas. Periksa bahwa dataset memiliki setidaknya tiga kolom.")
    except ValueError:
        st.warning("Terjadi kesalahan saat prapemrosesan data. Pastikan format data yang sesuai.")
else:
    st.warning("Dataset kosong atau tidak valid. Mohon unggah dataset yang valid.")
