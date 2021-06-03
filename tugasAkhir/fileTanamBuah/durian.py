from tkinter import *
from tkinter import ttk 

keterangan = """
    Nama Umum
    >> Durian
    Nama latin
    >> Fragaria
    Asal
    >> Chili & Amerika
    Prosedur Menanam
    >> Cara Menanam:
    1.  Pahami Syarat Tumbuh Pohon Durian
        a. Curah hujan pohon durian minimal 1500-3000 mm/tahun dan 3000/3500 mm/tahun.
        b. Pohon durian membutuhkan intensitas cahaya matahari sekitar 60%-80%.
        c. Pohon durian sebaiknya ditanam pada suhu rata-rata 20℃-30℃ untuk mendapatkan pertumbuhan yang optimal.
        d. Secara umum, pohon durian bisa tumbuh pada pada ketinggian 10 mdpl sampai 800 mdpl.
        e. Tipe tanah yang sesuai untuk menanam pohon durian adalah tanah lempung berpasir yang subur dengan banyak kandungan unsur organik.
    2. Pilih Bibit Unggul
        Pilihlah bibit unggul durian dengan ciri-ciri terlihat subur, banyak daunnya, dan batang yang kokoh.
    3. Persiapan Media Tanam
        Pohon durian bisa ditanam dengan mudah di pekarangan rumah, baik ditanam langsung di pekarangan atau menggunakan metode tabulampot.
        Media tanam dibuat dengan mencampur pupuk kandang dan tanah menggunakan perbandingan 1:1.
    4. Waktu Penanaman
        Waktu penanaman pohon durian paling ideal pada saat musim hujan.
    5. Pemupukan
        a. Dalam proses pemupukan, gemburkan tanah terlebih dahulu menggunakan sekop atau cangkul.
        b. Lalu campurkan pupuk dan sekam pada tanah tersebut menggunakan perbandingan 2:1.
        c. Gunakan pupuk organik seperti pupuk kompos atau pupuk kandang, karena pupuk tersebut tidak mengubah struktur tanah,
        d. Sedangkan untuk tabulampot, bisa menggunakan pupuk fosfor TSP dengan takaran 20 gram atau 2 sendok makan.
    6. Panen Durian
        a. Pohon durian yang ditanam dari bibit unggul biasanya membutuhkan waktu berbuah sekitar 4-5 tahun.
        b. Cara panennya bisa dibilang mudah, tapi pastikan buah durian jangan sampai jatuh menghantam tanah."""
window = Tk()  
window.title("Si-Tani (Petani Pintar")
window.configure(bg="LightCyan2")
window.state("zoomed")

kotak = Label(window, width = 150, height = 42 ,text = "" , bg = "LightCyan3").place(x = 200 , y = 20)

#buat isi
konten = Label(window, text = keterangan , bg = "LightCyan3", fg ="black", font = "Calibri 12 bold", justify = "left").place(x = 200 , y = 20)

#buat label halaman
welcome = Label(window, text = " Durian " , bg = "forest green", fg ="LightCyan2", font = "Calibri 20 bold").place(x = 0 , y = 30)

#buat tombol
back = Button(window, width = 10,height = 2, command = window.destroy, text = "Back", bg = "black", fg = "white", font = "Calibri 10 bold").place(x = 50,y = 600)

window.mainloop()    