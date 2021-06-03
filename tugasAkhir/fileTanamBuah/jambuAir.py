from tkinter import *
from tkinter import ttk 
keterangan = """    
    Nama Umum
    >> Jambu Air
    Nama latin
    >> Syzygium Aqueum
    Asal
    >> Indo Cina dan Indonesia
    Prosedur Menanam:
    Alat & Bahan
        a. Air                              g. Karet atau tali
        b. Ember                            h. Plastik
        c. Polibag                          i. Tanah
        d. Sekop kecil                      j. Pupuk kompos/kandang
        e. Cutter                           k. Hormon pertumbuhan
        f. Gunting setek

    Cara Menanam menggunakan biji
        a. Siapkan alat dan bahan.
        b. Campurkan tanah dengan pupuk kompos atau kandang.
        c. Kemudian taruh media tanam pada lubang tanam (jika langsung ditanam di tanah).
        d. Kemudian tanam biji jambu air pada lubang tanam yang sudah anda buat menggunakan kayu kecil. 
        e. Siram biji jambu air yang sudah ditanam."""

window = Tk()  
window.title("Si-Tani (Petani Pintar")
window.configure(bg="LightCyan2")
window.state("zoomed")

kotak = Label(window, width = 150, height = 42 ,text = "" , bg = "LightCyan3").place(x = 200 , y = 20)

#buat isi
konten = Label(window, text = keterangan , bg = "LightCyan3", fg ="black", font = "Calibri 12 bold", justify = "left").place(x = 200 , y = 20)

#buat label halaman
welcome = Label(window, text = " Jambu Air " , bg = "forest green", fg ="LightCyan2", font = "Calibri 20 bold").place(x = 0 , y = 30)

#buat tombol
back = Button(window, width = 10,height = 2, command = window.destroy, text = "Back", bg = "black", fg = "white", font = "Calibri 10 bold").place(x = 50,y = 600)

window.mainloop()    