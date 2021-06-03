from tkinter import *
from tkinter import ttk 
keterangan = """    
    Nama Umum
    >> Cabai
    Nama latin
    >> Capsicum frutescens
    Asal     
    >> Peru dan Meksiko
    Prosedur Menanam:
    1. Penyemaian cabai
        a. Masukkan tanah dan pupuk kandang dengan perbandingan 3:1 ke dalam polybag.
        b. Lindungi polybag dari hujan dan sinar matahari selama 1 minggu.
        c. Kemudian, rendam bibit cabai dalam air hangat selama 3 jam.
        d. Setelah itu, letakkan bibit cabai pada polybag dan tutupi kembali dengan tanah kira-kira kedalamannya 1 cm.
        e. Tunggu hingga benih cabai berkecambah, kurang lebih 4 minggu.
    2. Siapkan Polybag
        a. Polybag harus memiliki lubang yang berguna untuk sistem drainase tanaman cabai sehingga mencegah pembusukan.
        b. Lalu, isi pot dengan media tanam.
        c. Campurkan pupuk kompos.
        d. Batasnya 5-10 cm dari bibir pot dan jarak antar bijinya 5-10 cm
        e. Setelah itu, sebarkan bibit-bibit cabai yang sudah kamu pilih di atas media tanam.
    3. Siram Tanaman dengan Air Bersih
        Lakukan penyiraman dua kali sehari yaitu, pagi dan sore hari agar kelembapannya terjaga.
    4. Pisahkan Bibit Tanaman
        Biasanya setelah hari keempat, daun-daun pada tanaman cabai di polybag akan mulai tumbuh.
        Bila kamu ingin memanen cabai, pindahkanlah bibit cabai secara hati-hati ke dalam pot lain.
    5. Buatlah rambatan menggunakan batang kayu.
    6. Lakukan Perompesan
        Hilangkan tunas-tunas muda yang tumbuh di sekitar ketiak daun sebayak tiga kali hingga terbentuk cabang.
        Biasanya kegiatan perompesan dapat kamu mulai di hari ke-20 setelah tanam.
        Perompesan berguna agar tanaman tidak tumbuh ke samping ketika batang belum terlalu kuat untuk menopang.
"""

window = Tk()  
window.title("Si-Tani (Petani Pintar")
window.configure(bg="LightCyan2")
window.state("zoomed")

kotak = Label(window, width = 150, height = 42 ,text = "" , bg = "LightCyan3").place(x = 200 , y = 20)

#buat isi
konten = Label(window, text = keterangan , bg = "LightCyan3", fg ="black", font = "Calibri 12 bold", justify = "left").place(x = 200 , y = 20)

#buat label halaman
welcome = Label(window, text = "Cabai" , bg = "forest green", fg ="LightCyan2", font = "Calibri 20 bold").place(x = 0 , y = 30)

#buat tombol
back = Button(window, width = 10,height = 2, command = window.destroy, text = "Back", bg = "black", fg = "white", font = "Calibri 10 bold").place(x = 50,y = 600)

window.mainloop()    