import streamlit as st

st.title("From Data Diri")
st.write("Silahkan isi data diri anda")
st.write("Made by Kayla")

with st.form("form_data_diri"):
    nama = st.text_input("Nama")
    alamat = st.text_input("Alamat")
    email = st.text_input("Email")
    usia = st.number_input("Usia")
    submit = st.form_submit_button("Submit")

if submit:
    st.success(f"Terima kasih {nama} telah mengisi form data")
    st.write(f"Nama : {nama}")
    st.write(f"Alamat : {alamat}")
    st.write(f"Usia : {usia}")