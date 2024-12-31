import streamlit as st
import base64
import pandas as pd
import os
import csv
from datetime import time, date
from streamlit_option_menu import option_menu

st.markdown(""" 
<style>
    body {
        background-color: #f0f0f5;
        font-family: Arial, sans-serif;
    }

    .stButton>button {
        background-color: #3498db;
        color: white;
        font-size: 16px;
    }
            
    .stTextArea textarea, .stTextInput input {
        border: 1px solid #ffff;
        border-radius: 8px;
        padding: 8px;
    }

    .stTextArea textarea:focus, .stTextInput input:focus {
        border-color: #ffff;
    }

    .stSelectbox, .stDateInput, .stTimeInput {
        border: 1px solid #ffff;
        border-radius: 8px;
        padding: 8px;
    }

    .stSelectbox:focus, .stDateInput:focus, .stTimeInput:focus {
        border-color: #ffff;
    }

</style>
""", unsafe_allow_html=True)


# Untuk membaca gambar lokal dan mengkonversinya ke Base64
def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Mengubah gambar lokal menjadi Base64
image_path = "img/background (2).jpg"
image_base64 = image_to_base64(image_path)

# CSS Untuk Gambar Background
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{image_base64}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        height: 100vh;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar
with st.sidebar :
    selected = option_menu ("Pilihan Menu",
        ["Home","Tentang Kami", "Form","Struk Pemesanan", "Testimoni"],
        default_index=0,icons=["house", "info","pen", "book", "chat"], menu_icon=[" "])

# Membuat class person untuk menyimpan data user dan mengelola input
class person :
    
    # membuat konstruktor
    def __init__(self, nama=None, alamat=None, nomor=None , plat=None):
        self.nama = nama
        self.alamat = alamat
        self.nomor = nomor
        self.plat = plat
    
    # Membuat method input data daftar dan simpan di session_state agar saat pindah halaman tidak hilang
    def daftar (self):
        self.nama = st.text_input("Nama anda : ", st.session_state.get("nama", "")) 
        self.alamat = st.text_area("Alamat anda : ", st.session_state.get("alamat", ""))
        self.nomor = st.text_input("Nomor Telpon anda : ", st.session_state.get("nomor", ""))
        self.plat = st.text_input("Plat Kendaraan anda : ",st.session_state.get("plat", ""))

# Menyimpan data final yang sudah ke input ke session_state dan dapat digunakan di halaman lain
def simpan_data (simpan):
    st.session_state.nama = simpan.nama
    st.session_state.alamat = simpan.alamat
    st.session_state.nomor = simpan.nomor
    st.session_state.plat = simpan.plat


# Halaman home
if selected == "Home" :
    st.header("""Sentuhan Profesional untuk Kendaraan Bersih Sempurna""",)
    st.markdown("""
                Percayakan kebersihan kendaraan Anda pada kami. 
                Dengan sentuhan profesional, kami hadir untuk memastikan kendaraan 
                Anda selalu dalam kondisi bersih dan sempurna, kapan pun dan di mana pun.""")
    
    st.markdown("---")
    st.image ("img/content.jpg")
    st.subheader("Apa yang kami tawarkan?")
    tawar1, tawar2 = st.columns(2)
    tawar1.markdown("""
                1. Cepat dan Efisien
                2. Harga yang Kompetitif
                3. Pelayanan yang Profesional
                4. Kendaraan Bersih Sempurna 
                """)
    tawar2.markdown("""
                5. Bebas atur jadwal pemesanan Anda
                6. Keamanan dan Privasi yang Terjamin
                7. Garansi pencucian
                8. Alat -alat canggih 
                """)
# Halaman Tentang
if selected == "Tentang Kami":
    st.header("Pengenalan")
    st.markdown("""
                Hallo, kami adalah tim yang membuat aplikasi cuci steam yang bertujuan 
                untuk mempermudah dan sebagai solusi berbasis teknologi untuk pengembangan infrormasi dan booking pada 
                perusahaan steam, kami berharap aplikasi ini dapat membantu dan memberikan kemudahan bagi pengguna.
                karna kami berfokus pada desain yang user-friendly dan fungsional yang maksimal untuk perusahaan.
                kami tim pengembang yang beranggotakan :
                1. **Muhammad Ibnu Sabil**
                2. **Zhahara N Sukirman**
                3. **Iqbal Hermawan**
                """)
    
    st.markdown("---")
    st.header("Tim Pengembang Aplikasi")
    
    # Untuk gambar developer
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.image("img/abil.png", use_container_width=True)
        st.write("**Muhammad Ibnu Sabil**")
        st.write("Ketua Kelompok")

    with col2:
        st.image("img/zahara.png", use_container_width=True)
        st.write("**Zhahara N Sukirman**")
        st.write("Anggota")
    
    with col3:
        st.image("img/iqbal.png", use_container_width=True)
        st.write("**Iqbal Hermawan**")
        st.write("Anggota")
    
    st.markdown("---")
    st.header("Latar Belakang")
    st.markdown("""
                Layanan cuci kendaraan meningkat seiring bertambahnya jumlah kendaraan.
                Layanan ini cukup populer dikalangan masyarakat, karena hasilnya lebih baik, lebih bersih, lebih efisien dan ramah lingkungan, 
                namun sayangnya, banyak pelanggan mengalami kesulitan mendapatkan layanan yang cepat dan nyaman. 
                1. Penyedia jasa cuci steam menghadapi masalah manajemen waktu dan antrian yang panjang. 
                2. Pelanggan sering kali tidak mendapatkan pelayanan yang memuaskan karena antrian yang penuh. 
                
                dengan aplikasi cuci steam yang menawarkan solusi digital dengan kemampuan untuk booking layanan secara online, 
                mengetahui waktu tunggu, dan berbagai paket layanan. Aplikasi ini memberikan kemudahan bagi pelanggan 
                dan meningkatkan efisiensi operasional penyedia layanan cuci kendaraan.
                """)

    st.markdown("---")
    st.header ("Manfaat, apa yang didapat?")
    st.markdown("""
                Manfaat yang didapatkan pebngguna dengan menggunakan aplikasi ini adalah :
                1. **Kemudahaan Akses** : Membantu pengguna untuk mendapatkan informasi tentang layanan cuci steam tanpa ketempan steam.
                2. **Meningkatkan Efisiensi** : Membantu pengguna untuk mengetahui waktu jam dan tanggal berapa mereka booking.
                3. **Meningkatkan Kualitas** : Dengan sistem pemesanan yang lebih cepat, pengalaman pelanggan secara keseluruhan akan meningkat, 
                                            mulai dari proses pemesanan hingga penyelesaian layanan.
                4. **Pengelola Antrian yang lebih baik** : Penyedia jasa dapat melihat pesanan masuk secara real-time dan mengatur jadwal sesuai dengan kapasitas operasional.
                5. **Penghematan Biaya Operasional** : Aplikasi membantu mengoptimalkan sumberdaya mengurangi biaya manual untuk pencatatan dan pengelolaan antrian, serta meminimalkan kesalahan manusia.
                """)
        
    


# Membuat data formulir identitas 
if selected == "Form" :
    st.title("Formulir Identitas Customer")           
    
    #Menjalankan input 
    customer = person () # membuat objek customer dari class person
    customer.daftar() # menampilkan form 
    simpan_data(customer) # Data disimpan ke session_state dan dapat digunakan di halaman lain

    st.markdown("---")
    st.subheader("Menu Harga Pemesanan")
    # Membuat fungsi harga kendaraan dan harga paket kendaraan 
    def harga_kendaraan (harga): #harga_kendaraan menerima input yang diberikan oleh user pada dropdown
        if harga == "Motor Kecil - Rp 15.000": #parameter (harga) untuk menyimpan pilihan jenis harga kendaraan yang dipilih oleh user dan menampilkan harga
            return 15000
        elif harga == "Motor Besar - Rp 20.000":
            return 20000
        elif harga == "Mobil Kecil - Rp 50.000":
            return 50000
        elif harga == "Mobil Besar - Rp 60.000":
            return 60000
        else:
            return 0
    
    def harga_paket_kendaraan (paket): #harga_paket_kendaraan menerima input yang diberikan oleh user pada dropdown
            if paket == "Paket Basic": #parameter (paket) untuk menyimpan pilihan jenis paket kendaraan yang dipilih oleh user dan menampilkan harga dari paket
                return 40000
            elif paket == "Paket Standar":
                return 70000
            elif paket == "Paket Premium":
                return 100000
            else:
                return 0
    
    # Membuat value pilihan Menu harga || jenis kendaran, harga kendaraan, paket kendaraan dan menyimpan dalam session_state
    kendaraan = st.selectbox("Jenis Kendaraan anda : ", 
                            [" ", "Motor Kecil 100 – 150 cc", 
                            "Motor Besar 250 – 1.000 cc", "Mobil Kecil 1.000 – 1.500 cc", 
                            "Mobil Besar 2.000 – 3.500 cc"],
                            index = [" ", "Motor Kecil 50 – 150 cc", 
                            "Motor Besar 250 – 1.000 cc", "Mobil Kecil 1.000 – 1.500 cc", 
                            "Mobil Besar 2.000 – 3.500 cc"].index(st.session_state.get("kendaraan", " ")))
    
    pilih_harga = st.selectbox("Harga cuci kendaraan : ", 
                                [" ", "Motor Kecil - Rp 15.000", 
                                "Motor Besar - Rp 20.000", "Mobil Kecil - Rp 50.000", 
                                "Mobil Besar - Rp 60.000"],
                                index =[" ", "Motor Kecil - Rp 15.000", 
                                "Motor Besar - Rp 20.000", "Mobil Kecil - Rp 50.000", 
                                "Mobil Besar - Rp 60.000"].index(st.session_state.get("harga", " ")))
    
    paket1, paket2, paket3 = st.columns(3)
    paket1.write("""Paket Basic : Pembersihan eksterior lebih menyeluruh, termasuk pembersihan jendela dan velg. Bisa ditambahkan pembersihan interior ringan.    Rp 40.000""")
    paket2.write("""Paket Standar : Pembersihan menyeluruh dengan steam, termasuk eksterior dan interior (dashboard, jok, dan karpet). Pembersihan detail pada bagian mesin dan kabin. Rp 70.000""")
    paket3.write("""Paket Premium : Layanan cuci steam lengkap dengan pembersihan eksterior, interior, mesin, dan detailing khusus seperti wax atau perlindungan cat. Rp 100.000 """)
    pilih_paket = st.selectbox("Paket cuci kendaraan :", 
                                [" ", "Tidak Memilih Paket", 
                                "Paket Basic", "Paket Standar", "Paket Premium"],
                                index = [" ", "Tidak Memilih Paket", 
                                "Paket Basic", "Paket Standar", "Paket Premium"].index(st.session_state.get("paket", " ")))
    
    # Memanggil fungsi,memberikan parameter dan variabel untuk disimpan dalam variabel
    hargaKendaraan = harga_kendaraan(pilih_harga)
    hargaPaket = harga_paket_kendaraan(pilih_paket)
    
    # Simpan data dalam session_state
    st.session_state.kendaraan = kendaraan
    st.session_state.harga = pilih_harga
    st.session_state.harga_kendaraan = hargaKendaraan
    st.session_state.paket = pilih_paket
    st.session_state.harga_paket_kendaraan = hargaPaket


    st.markdown("---")
    st.subheader("Jadwal Reservasi")    
    # Membuat input tanggal dan jam
    tanggal = st.date_input ("Tanggal Pesan : ", st.session_state.get("tanggal", date.today()))
    tanggal_rsv = st.date_input ("Tanggal Pencucian : ", st.session_state.get("tanggal_rsv", date.today()))
    waktu = st.time_input("Waktu Oprasional dari jam 09.00 hingga 17.00",st.session_state.get("waktu", time(9, 0)))
    
    # Jam oprasional dimulai dan diakhiri
    jam_mulai = time(9, 0)
    jam_akhir = time(17, 0)
    # Menggunakan while untuk memastikan waktu yang dipilih dalam jam operasioanal
    if waktu < jam_mulai or waktu > jam_akhir :
        st.warning ("Waktu yang dipilih melebihi jam yang diminta. mohon isi ulang kembali")
    
    # Menyimpan data dalam session state
    st.session_state.tanggal = tanggal
    st.session_state.tanggal_rsv = tanggal_rsv
    st.session_state.waktu = waktu
    
    # Membuat button simpan 
    if st.button("Simpan"):
        if kendaraan==" " or pilih_harga==" " or pilih_paket==" " :
            st.error("Maaf jenis kendaraa, harga, atau paket belum dipilih")
        elif not waktu or not tanggal or not tanggal_rsv :
            st.error("Maaf tanggal pesan, tanggal pencucian, atau waktu belum dipilih")
        elif not customer.nama or not customer.alamat or not customer.nomor or not customer.plat:
            st.error("Maaf data identitas anda belum lengkap")
        elif waktu < jam_mulai or waktu > jam_akhir :
            st.error("Waktu yang dipilih melebihi jam oprasional")
        else:
            st.success("Pesanan Telah berhasil tersimpan!")
            
if selected == "Struk Pemesanan" :
    st.title("Struk Pemesanan")
    # Memanggil dan menyimpan data dari session state sebelumnya
    nama = st.session_state.get("nama", "-")  
    alamat = st.session_state.get("alamat", "-")
    nomor = st.session_state.get("nomor", "-")
    plat = st.session_state.get("plat", "-")
    kendaraan = st.session_state.get("kendaraan", "-")
    hargaKendaraan = st.session_state.get("harga_kendaraan", 0)
    pilih_paket = st.session_state.get("paket", "-")
    hargaPaket = st.session_state.get("harga_paket_kendaraan", 0)
    tanggal = st.session_state.get("tanggal", date.today())
    tanggal_rsv = st.session_state.get("tanggal_rsv", date.today())
    waktu = st.session_state.get("waktu", time(9, 0))
    
    # Rumus menghitung total harga
    total_harga = hargaKendaraan + hargaPaket
    
    # Membuat key-value atau kata kunci nilai untuk data struk dan data total
    data_struk = {
    "Keterangan": ["Nama", "Alamat", "Nomor Telepon", "Plat Kendaraan", 
                "Jenis Kendaraan", "Harga Kendaraan", "Paket Kendaraan", 
                "Harga Paket","Tanggal Pesan", "Tanggal Reservasi", "Waktu Pencucian"],
    "Detail": [nama, alamat, nomor, plat, kendaraan, f"Rp {hargaKendaraan:,}", 
            pilih_paket, f"Rp {hargaPaket:,}",tanggal, tanggal_rsv, waktu]}
    data_total = {"Total" : ["Total Harga"],
                "Detail" : [f"Rp {hargaKendaraan:,} + Rp {hargaPaket:,} = Rp {total_harga:,}"]}
    
    # Membuat DataFrame dari dictionary
    df_struk = pd.DataFrame(data_struk)
    df_total = pd.DataFrame(data_total)
    
    # Menampilkan struk dan total dalam bentuk tabel
    st.table(df_struk)
    st.subheader("Total Pemesanan") # membuat subheader
    st.table(df_total)
    
    # Membuat fungsi valid dapat di download, menyimpan data pada csv dan restart
    def valid_pemesanan():
        if kendaraan ==" " or hargaKendaraan == 0 or hargaPaket == 0 :
                return False,"Maaf jenis kendaraa, harga, atau paket belum dipilih"
        elif not waktu or not tanggal or not tanggal_rsv :
                return False,"Maaf tanggal pesan, tanggal pencucian, atau waktu belum dipilih"
        elif not nama or not alamat or not nomor or not plat:
                return False,"Maaf data identitas anda belum lengkap"
        else: # Jikas hasil true maka akan muncul botton dw
            data_pemesanan = {
                "Nama": nama,
                "Alamat": alamat,
                "Nomor Telepon": nomor,
                "Plat Kendaraan": plat,
                "Jenis Kendaraan": kendaraan,
                "Harga Kendaraan": hargaKendaraan,
                "Paket Kendaraan": pilih_paket,
                "Harga Paket": hargaPaket,
                "Tanggal Pesan": tanggal,
                "Tanggal Reservasi": tanggal_rsv,
                "Waktu Pencucian": waktu
            } 
            data_csv(data_pemesanan)
            return True, "Pemesanan Berhasil terkonfirmasi"
    
    def data_csv(data) : # membuat fungtion untuk menyimpan data ke csv
        df = pd.DataFrame([data])
        df.to_csv('data_pemesanan.csv', index=False )
    
    def restart_pesanan(): # membuat fungsi untuk mengulang pemesanan
            st.session_state.clear()
    
    # membuat button batal dan simpan untuk mengvalidasi pemesanan
    Oke, batal = st.columns(2)
    with Oke:
        if st.button("Oke"):
            valid, pesan = valid_pemesanan( )
            if valid :
                st.success(pesan)
                if os.path.exists("data_pemesanan.csv"): # memeriksa apakah file csv sudah ada di dalam direktori
                    st.download_button( #membuat button dw
                        label="Download Struk Pemesanan", # label button
                        data=open("data_pemesanan.csv", "rb").read(), # file yang akan di download
                        file_name="struk_pemesanan.csv", # nama file yang akan di download
                        mime="text/csv" # tipe file yang akan di download
                        )
            else :
                st.error(pesan) # jika pemesanan tidak valid maka akan muncul pesan error
                
    with batal:
        if st.button("Batal"):
            restart_pesanan()
            st.info("Pesanan telah dibatalkan")
            

if selected == "Testimoni" :
    st.title("Testimoni")
    
    # membuat nama file csv
    file_testimoni = "Testimoni.csv" 
    
    # membuat fungsi untuk menyimpan testimoni ke dalam file csv
    def simpan_testimoni (nama, testimoni):
        file1 = os.path.isfile(file_testimoni)
        with open(file_testimoni, mode="a", newline="", encoding="utf-8") as file: # mode a sebagai data akan ditambah di akhir file tanpa menghapus isi yang sudah ada
            writer = csv.writer(file)                                              # newline "" mencegah penambahan baris kosong di antara setiap baris pada file CSV 
            # Membuat objek writer yang digunakan                                  # encoding=utf-8 digunakan untuk mendukung karakter Unicode (seperti karakter non-ASCII).
            # untuk menulis data ke dalam file CSV.
            if not file1:                                                        
                writer.writerow(["Nama", "Testimoni"])
            # membuat header jika file csv belum ada
            writer.writerow([nama, testimoni])
    # membuat fungsi untuk membaca testimoni dari file csv
    def baca_testimoni():
        if os.path.exists(file_testimoni): # memastikan file_tstimoni berada pada sistem/directory
            with open(file_testimoni, mode="r", newline="", encoding="utf-8") as file : # mode r untuk mode membaca | newline=""" mencegah penambahan baris kosong | encoding="utf-8" memastikan bahwa karakter non-ASCII dapat dibaca dengan benar.
                reader = csv.reader(file) # membuat objek reader untuk membaca data dari file CSV.
                next(reader) # untuk melewati baris sebelumnya pada isi file testimoni.csv
                return list(reader) # mengubah isi file menjadi daftar list
        return [] # untuk isi file_testimoni tidak terdaftar, maka akan mengembalikan nilai kosong
    
    st.write("Berikut adalah testimoni dari pelanggan kami")
    customer = st.text_input("Nama anda :")
    comment = st.text_area("Ulasan anda :")
    
    #membuat tombol button submit untuk menampilkan testimoni 
    if st.button("Submit"): 
            if customer and comment: # memastikan custumor dan comment sudah di isi
                simpan_testimoni(customer, comment) # memanggil fungsi
                st.success("Testimoni telah terkirim") # jika testimoni berhasil terkirim maka akan muncul pesan success
            else :
                st.error("Mohon isi semua form") # jika form belum di isi maka akan muncul pesan error
            
    urutan = baca_testimoni() # memanggil fungsi baca testimoni
    if urutan :
        st.subheader("Ulasan Pengguna")
        st.markdown("---") # membuat garis horizontal
        for i, row in enumerate(urutan, start=1): # untuk mengurutkan testimoni berdasarkan uruta, enumerate() untuk mengiterasi urutan
            if len(row) >= 2:
                user = row [0] # kolom pertama,mengambil nama user
                pesan = row [1] # kolom kedua,mengambil pesan user
                st.write(f"**{i}. {user}**") # menampilkan nama pengguna
                st.write(f"{pesan}")
                st.markdown("---")
    else:
        st.write("Belum ada ulasan") # jika testimoni belum ada maka akan muncul pesan belum ada ulasan