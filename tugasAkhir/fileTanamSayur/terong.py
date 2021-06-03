from tkinter import *
from tkinter import ttk 
keterangan = """    
    Nama Umum
    >> Terong
    Nama latin
    >> Solanum melongena
    Asal     
    >> India dan Sri Lanka
    Prosedur Menanam:
    1. Pemilihan Bibit
        Kondisi bibit bersih, mengkilat, berwarna seragam dan berdaya kecambah 80%.
    2. Persiapan Tanam
        a. Tanah dalam kondisi gembur dan kaya zat organik.
        b. siapkan polybag berukuran besar, padi sekam dan air secukupnya.
    3. Penyemaian di Pot
        a. Rendamlah benih terong di dalam air hangat sekitar 15 menit.
        b. Campurkan tanah dan sekam dan masukan ke dalam polybag.
        c. Buatlah lubang dengan jarak antar lubang minimal 1 cm.
        d. Letakan benih pada lubang dan tutup lubang menggunakan campuran tanah dan sekam secukupnya.
        e. Padatkan tanah dengan menepuk-nepuk.
        f. Siram secara teratur dan taruh di tempat dengan sinar matahari yang cukup hingga 1 bulan sampai kecambah muncul. 
    4. Pemindahan benih
        a. Siapkan lubang dnegan kedalaman 5 cm.
        b. Letakan benih di lubang dan tutup dengan campuran tanah dan sekam.
        c. Siram secar teratur.
    5. Pemliharaan
        a. Pasang batang bambu sebagai penyangga.
        b. Siram secara teratur serta beri pupuk organik tambahan.
        c. Cabut gulma-gulma yang ada di sekitar tanaman dan potong daun-daun yang tak sehat
    6. Panen
        a. Tanaman telah berumur 3-4 bulan.
        b. Petik menggunakan gunting.
        c. Petiklah pada saat pagi atau sore hari.
"""

window = Tk()  
window.title("Si-Tani (Petani Pintar")
window.configure(bg="LightCyan2")
window.state("zoomed")

kotak = Label(window, width = 150, height = 42 ,text = "" , bg = "LightCyan3").place(x = 200 , y = 20)

#buat isi
konten = Label(window, text = keterangan , bg = "LightCyan3", fg ="black", font = "Calibri 12 bold", justify = "left").place(x = 200 , y = 20)

#buat label halaman
welcome = Label(window, text = "Terong" , bg = "forest green", fg ="LightCyan2", font = "Calibri 20 bold").place(x = 0 , y = 30)

#buat tombol
back = Button(window, width = 10,height = 2, command = window.destroy, text = "Back", bg = "black", fg = "white", font = "Calibri 10 bold").place(x = 50,y = 600)

window.mainloop()    