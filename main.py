#import library
import streamlit as st
import pandas as pd
import openpyxl
import plotly.express as px
from matplotlib import pyplot as plt
from streamlit_extras.dataframe_explorer import dataframe_explorer
from streamlit_option_menu import option_menu

#config halaman
st.set_page_config(page_title="Home", page_icon=":bar_chart:", layout="wide")

#load dataset
df = pd.read_csv('hasil_forecast_model.csv')

# Remove the unnamed column if it exists
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
#sidebar
st.sidebar.image("image/logo_tim.png")
with st.sidebar:
    st.title("Pilih Tanggal")
    start_date = st.date_input(label="Start Date")

with st.sidebar:
    end_date = st.date_input(label="End Date")

df2 = df[(df["Tanggal"] >= str(start_date)) & (df["Tanggal"] <= str(end_date))]

selected = option_menu(
    menu_title="Menu",
    options=["Home", "Temperature", "pm2.5", "Kondisi Cuaca", "Kualitas Udara", "Rekomendasi", "About Team"],
    icons=["🏠", "🌡️", "🌬️", "🌦️", "🌫️", "📝", "📖"],
    orientation="horizontal",
)


if selected == "Home":
    st.warning("Data Hanya Mencakup tanggal dalam rentang  2016-07-01 sampai 2018-12-18")
    st.success("Kamu Memilih Tanggal Dari: " + str(start_date) + " Sampai " + str(end_date))
    st.title("Home")
    if not df2.empty:
        filter = dataframe_explorer(df2, case=False)
        st.dataframe(filter, use_container_width=True)
    else:
        st.write("Tidak ada data dalam rentang tanggal yang dipilih.")

if selected == "Temperature":
    st.warning("Data Hanya Mencakup tanggal dalam rentang  2016-07-01 sampai 2018-12-18")
    st.success("Kamu Memilih Tanggal Dari: " + str(start_date) + " Sampai " + str(end_date))
    st.title("Temperature")
    if not df2.empty:
        a1, a2 = st.columns(2)

        with a1:
            st.subheader("Waktu & Temperature")
            fig = px.line(df2, x='Tanggal', y='Temperature', title='Temperature Over Time')
            fig.update_layout(xaxis_title='Tanggal', yaxis_title='Temperature')
            st.plotly_chart(fig, use_container_width=True)

        with a2:
            st.subheader("Data Metrics Temperature")
            from streamlit_extras.metric_cards import style_metric_cards

            col1, col2 = st.columns(2)
            col1.metric(label="Min", value=df2['Temperature'].min(), delta="Temperature Terendah", delta_color="normal")
            col2.metric(label="Max", value=df2['Temperature'].max(), delta="Temperature Tertinggi", delta_color="inverse")

            col11, col22 = st.columns(2)
            col11.metric(label="Mean", value=df2['Temperature'].mean(), delta="Temperature Rata-rata", delta_color="normal")
            col22.metric(label="Range", value=df2['Temperature'].max() - df2['Temperature'].min(), delta="Range", delta_color="inverse")

            style_metric_cards(background_color="lightblue")
    else:
        st.write("Tidak ada data untuk Temperature dalam rentang tanggal yang dipilih.")

if selected == "pm2.5":
    st.warning("Data Hanya Mencakup tanggal dalam rentang  2016-07-01 sampai 2018-12-18")
    st.success("Kamu Memilih Tanggal Dari: " + str(start_date) + " Sampai " + str(end_date))
    st.title("pm2.5")
    if not df2.empty:
        b1, b2 = st.columns(2)

        with b1:
            st.subheader("Waktu & PM2.5")
            fig_pm25 = px.line(df2, x='Tanggal', y='pm2.5', title='PM2.5 Over Time')
            fig_pm25.update_layout(xaxis_title='Tanggal', yaxis_title='PM2.5')
            st.plotly_chart(fig_pm25, use_container_width=True)

        with b2:
            st.subheader("Data Metrics PM2.5")
            from streamlit_extras.metric_cards import style_metric_cards

            col1, col2 = st.columns(2)
            col1.metric(label="Min", value=df2['pm2.5'].min(), delta="PM2.5 Terendah", delta_color="normal")
            col2.metric(label="Max", value=df2['pm2.5'].max(), delta="PM2.5 Tertinggi", delta_color="inverse")

            col11, col22 = st.columns(2)
            col11.metric(label="Mean", value=df2['pm2.5'].mean(), delta="PM2.5 Rata-rata", delta_color="normal")
            col22.metric(label="Range", value=df2['pm2.5'].max() - df2['pm2.5'].min(), delta="Range", delta_color="inverse")

            style_metric_cards(background_color="lightblue")
    else:
        st.write("Tidak ada data untuk PM2.5 dalam rentang tanggal yang dipilih.")

if selected == "Kondisi Cuaca":
    st.warning("Data Hanya Mencakup tanggal dalam rentang  2016-07-01 sampai 2018-12-18")
    st.success("Kamu Memilih Tanggal Dari: " + str(start_date) + " Sampai " + str(end_date))
    st.title("Kondisi Cuaca")
    if not df2.empty:
        st.subheader("Histogram Kondisi Cuaca")
        fig, ax = plt.subplots()
        if not df2['Kondisi Cuaca'].empty:
            ax.hist(df2['Kondisi Cuaca'], bins=12)
            ax.set_title("Histogram Kondisi Cuaca")
            ax.set_xlabel("Kondisi Cuaca")
            ax.set_ylabel("Frequency")
            st.pyplot(fig)
        else:
            st.write("Tidak ada data untuk Kondisi Cuaca dalam rentang tanggal yang dipilih.")
    else:
        st.write("Tidak ada data dalam rentang tanggal yang dipilih.")

if selected == "Kualitas Udara":
    st.warning("Data Hanya Mencakup tanggal dalam rentang  2016-07-01 sampai 2018-12-18")
    st.success("Kamu Memilih Tanggal Dari: " + str(start_date) + " Sampai " + str(end_date))
    st.title("Kualitas Udara")
    if not df2.empty:
        st.subheader("Histogram Kualitas Udara")
        fig2, ax2 = plt.subplots()
        if not df2['Kualitas Udara'].empty:
            df2['Kualitas Udara'].value_counts().plot(kind='bar', ax=ax2)
            ax2.set_title("Histogram Kualitas Udara")
            ax2.set_xlabel("Kualitas Udara")
            ax2.set_ylabel("Frequency")
            st.pyplot(fig2)
        else:
            st.write("Tidak ada data untuk Kualitas Udara dalam rentang tanggal yang dipilih.")
    else:
        st.write("Tidak ada data dalam rentang tanggal yang dipilih.")

if selected == "Rekomendasi":
    st.warning("Data Hanya Mencakup tanggal dalam rentang  2016-07-01 sampai 2018-12-18")
    st.success("Kamu Memilih Tanggal Dari: " + str(start_date) + " Sampai " + str(end_date))
    st.title("Rekomendasi Sektor Pariwisata")
    if not df2.empty:
        st.subheader("Rekomendasi Berdasarkan Destinasi")
        if all(column in df2.columns for column in ["Tanggal", "Destinasi"]):
            rekomendasi_destinasi_df = df2[["Tanggal", "Destinasi"]].drop_duplicates().reset_index(drop=True)
            st.dataframe(rekomendasi_destinasi_df, use_container_width=True)
        else:
            st.write("Dataframe tidak memiliki kolom yang diperlukan untuk rekomendasi.")

        st.subheader("Rekomendasi Berdasarkan Aktivitas")
        if all(column in df2.columns for column in ["Tanggal", "Aktivitas"]):
            rekomendasi_aktivitas_df = df2[["Tanggal", "Aktivitas"]].drop_duplicates().reset_index(drop=True)
            st.dataframe(rekomendasi_aktivitas_df, use_container_width=True)
        else:
            st.write("Dataframe tidak memiliki kolom yang diperlukan untuk rekomendasi.")

        st.subheader("Rekomendasi Berdasarkan Kesehatan")
        if all(column in df2.columns for column in ["Tanggal", "Rekomendasi"]):
            rekomendasi_rekomendasi_df = df2[["Tanggal", "Rekomendasi"]].drop_duplicates().reset_index(drop=True)
            st.dataframe(rekomendasi_rekomendasi_df, use_container_width=True)
        else:
            st.write("Dataframe tidak memiliki kolom yang diperlukan untuk rekomendasi.")
    else:
        st.write("Tidak ada data dalam rentang tanggal yang dipilih.")




if selected == "About Team":
    st.title("Tentang Kami")
    st.subheader("Neural Net Wizard")
    st.image("image/logo_tim.png")
    st.write("""
    Kami adalah Tim Neural Net Wizard yang terdiri dari mahasiswa berdedikasi tinggi dari Kompi 28 yang mengikuti program Merdeka Belajar Kampus Merdeka (MSIB) Batch 6 di Startup Campus. Fokus utama kami adalah memperdalam pengetahuan dan keterampilan di bidang Data Science dan Artificial Intelligence (AI).

    Tim Final Project kami terdiri dari:
    
    - Syifa Gumay               - Universitas Diponegoro
    - Aulia Nailul Fithria      - Institut Teknologi Sepuluh Nopember
    - Ariansyah Aryo Prasetio   - Politeknik Negeri Tanah Laut
    - Gessya Saefani            - Universitas Islam Bandung
    - I Made Danu Dwiyadnyana   - Universitas Pendidikan Ganesha
    - Khairunnisa Diva Mustafa  - Universitas Jenderal Soedirman
    - Muthiya Azka Azzahra      - Universitas Diponegoro
    
    Kami sangat berterima kasih kepada Kak Wiranda atas bimbingan dan arahan beliau sebagai mentor. Kami juga sangat mengapresiasi dukungan dan tindak lanjut yang diberikan oleh Kak Dara sebagai fasilitator. Dedikasi mereka sangat berharga dalam perjalanan kami untuk menjadi Data Scientist dan AI Engineer yang kompeten.
    """)

