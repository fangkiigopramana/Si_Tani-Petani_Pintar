from tkinter import *
from tkinter import ttk 
keterangan = """    
    Nama Umum
    >>Mentimun
    Nama latin
    >> Cucumis sativus
    Asal     
    >> Asia Utara
    Prosedur Menanam:
    1. Persiapan Lahan
        a. Anda bisa melakukan penggemburan tanah supaya subur dengan cara dicangkul.
        b. Buat bedengan dengan ukuran 1×5 meter dengan tinggi 30cm, dan jarak antar bedengan 50cm. 
        c. Buat lubang tanam yang memiliki kedalaman sekitar 20 cm, sementara jarak antara lubang tanam adalah 50×60 cm. 
        d. Masukkan pupuk kompos ataupun pupuk kandang ke setiap lubang tanam, lalu diamkan hingga satu minggu.
    2. Penyemaian
        a. Siapkan polybag yang berisikan tanah dan pupuk kompos / pupuk kandang dengan komposisi yang seimbang.
        b. Benih biasanya mulai tumbuh pada umur 14 hari.
        c. Setelah bibit siap, maka secepatnya pindahkan bibit dari media semai ke media tanam
    3. Pemangkasan
        a. Memangkas tunas yang bertujuan untuk menyisakan tiga tunas yang dapat menghasilkan buah.
        b. Semakin banyak tunas yang dipertahankan maka akan semakin lama tanaman dapat menghasilkan buah.
        c. Pemangkasan tunas dapat dimulai pada usia 1 hingga 1,5 bulan setelah tanam dan dilakukan pada saat tanaman tidak sedang berbunga.
    4. Pemupukan
        Pupuk harus dilakukan sejak tanaman dipindah dari media semai ke media tanam, sampai dengan memasuki masa panen. 
    5. Pengontrolan
        Yang dikontrol disini bukan buah yang keluar dari setiap tanaman, tapi lebih ke kekuatan tanaman yang akan menyangga buah tersebut."""

window = Tk()  
window.title("Si-Tani (Petani Pintar")
window.configure(bg="LightCyan2")
window.state("zoomed")

kotak = Label(window, width = 150, height = 42 ,text = "" , bg = "LightCyan3").place(x = 200 , y = 20)

#buat isi
konten = Label(window, text = keterangan , bg = "LightCyan3", fg ="black", font = "Calibri 12 bold", justify = "left").place(x = 200 , y = 20)

#buat label halaman
welcome = Label(window, text = "Mentimun" , bg = "forest green", fg ="LightCyan2", font = "Calibri 20 bold").place(x = 0 , y = 30)

#buat tombol
back = Button(window, width = 10,height = 2, command = window.destroy, text = "Back", bg = "black", fg = "white", font = "Calibri 10 bold").place(x = 50,y = 600)

window.mainloop()    