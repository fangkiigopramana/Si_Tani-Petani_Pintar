from tkinter import *
from tkinter import ttk 
keterangan = """    
    Nama Umum
    >> Mangga
    Nama latin
    >> Mangifera Indica
    Asal     
    >> India & Burma
    
    Prosedur Menanam:
    1. Alat & Bahan:
        a. Ambil mangga yang sangat matang, dan potong buahnya secara hari-hati.
        b. Keluarkan benih dan buang sekam.
        c. lubangi bagian bawah pot untuk drainase. 
        d. Tempatkan benih di dalam pot dengan mata menghadap ke atas.
        e. Basahi tanah sedikit.
        f. Tutupi benih dengan setengah inci (1,27 cm) tanah. 
        g. Benih tumbuh selama seminggu dengan disiram secukupnya secara berkala"""

window = Tk()  
window.title("Si-Tani (Petani Pintar")
window.configure(bg="LightCyan2")
window.state("zoomed")

kotak = Label(window, width = 150, height = 42 ,text = "" , bg = "LightCyan3").place(x = 200 , y = 20)

#buat isi
konten = Label(window, text = keterangan , bg = "LightCyan3", fg ="black", font = "Calibri 12 bold", justify = "left").place(x = 200 , y = 20)

#buat label halaman
welcome = Label(window, text = "Mangga" , bg = "forest green", fg ="LightCyan2", font = "Calibri 20 bold").place(x = 0 , y = 30)

#buat tombol
back = Button(window, width = 10,height = 2, command = window.destroy, text = "Back", bg = "black", fg = "white", font = "Calibri 10 bold").place(x = 50,y = 600)

window.mainloop()    