from tkinter import *
from tkinter import ttk 

keterangan = """
    Nama Umum
    >> Apel
    Nama latin
    >> Malus domestica
    Asal
    >> Asia Tengah
    Prosedur Menanam    
    >> Buah apel dapat ditanam dengan cara stek atau cangkok juga dengan menggunakan bijinya. 
    A. Cara tanam menggunakan biji

    1. Tahap biji berkecambah
        a.  Pilih benih biji kualitas bagus
        b.  Selanjutnya letakkan biji-biji tersebut hingga kulit bagian luarnya menjadi kering.
        c.  Setelah itu, bungkus biji tadi menggunakan tisu basah dan masukkan ke dalam wadah yang tertutup rapat. 
        d.  Letakkan benih kedalam lemari es dengan suhu 4,4 – 10 derajat Celcius selama 8 minggu agar keluar tunasnya.
        e.  Setelah 8 minggu, keluarkan dari kulkas dan biji ini siap untuk dipindahkan pada media tanah.

    2. Memindahkan benih berkecambah kedalam pot
        a.  Siapkan wadah berupa pot kecil yang telah diisi dengan tanah pH netral. Tidak perlu dicampurkan pupuk.
        b.  Buat cekungan pada tanah dan letakkan benih biji tersebut pada cekungan tanah dengan hati-hati, lalu tutupi dengan tanah.
        c.  Tepuk-tepuk tanah dengan lembut. Kemudian, sirami dengan air agar tanahnya tetap lembab.
        d.  Tempatkan pada suhu kamar dan berikan paparan sinar matahari secara langsung.

    3. Memindahkan pohon apel kecil pada lahan tanah
        Yang harus diperhatikan adalah, ketika benih yang telah Anda tanam pada pot kecil sudah tumbuh hingga setinggi 25cm. 
        Anda harus melakukan hal-hal berikut:
        a.  Tanam pada lahan yang lembab dengan pH yang netral.
        b.  Berikan lahan yang dapat terkena sinar matahari langsung. Kalau bisa, tanam menghadap ke arah timur.
        c.  Pastikan memberikan ruang yang luas untuk tumbuh akarnya nanti, 
            sebab akan diberi jarak antara pohon muda yang satu dengan yang lainnya sekitar 4,5 atau 5 meter.
        d.  Siram pohon kecil Anda sebanyak 10 sampai 12 hari. Namun ketika sudah tumbuh besar, bisa dikurangi penyiramannya.
            Pohon apel yang ditanam pada lahan harus tetap diberikan perawatan hingga tumbuh besar dan berbuah.
         """

window = Tk()  
window.title("Si-Tani (Petani Pintar")
window.configure(bg="LightCyan2")
window.state("zoomed")

#buat isi
konten = Label(window, text = keterangan , bg = "LightCyan3", fg ="black", font = "Calibri 12 bold", justify = "left").place(x = 200 , y = 20)

#buat label halaman
welcome = Label(window, text = " Apel" , bg = "forest green", fg ="LightCyan2", font = "Calibri 20 bold").place(x = 0 , y = 30)

#buat tombol
back = Button(window, width = 10,height = 2, command = window.destroy, text = "Back", bg = "black", fg = "white", font = "Calibri 10 bold").place(x = 50,y = 600)

window.mainloop()    