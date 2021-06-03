from tkinter import * 
from tkinter import ttk
from tkinter import messagebox

#main
window = Tk()  
window.title("Si-Tani (Petani Pintar")
window.configure(bg="LightCyan2")
window.state("zoomed")
#buat fungsi

def jual():
    #kotak
    kotak = Label(window, width = 130, height = 25 ,text = "" , bg = "LightCyan3").place(x = 200 , y = 120)
    getter = ("Nama barang\t\t\t\t\t:\t" + stringnama.get() +"\n\n\n" + "Kuantitas\t\t\t\t\t:\t" + str(intkuantitas.get()) + "\n\n\n" + "Harga (per kg)\t\t\t\t\t:\t" + str(intharga.get()))
    Label(window, text= getter ,bg = "LightCyan3", fg = "forest green", font = "Calibri 15 bold", justify = "left").place(x = 250, y = 200)
    notify = "Setelah barang terjual, uang akan dikirimkan ke rekening tersebut.\nTerima kasih"
    Label(window, text= notify, justify = "left", bg  ="LightCyan3", fg = "forest green", font = "Calibri 15 bold").place(x = 250, y = 420)

    Label(window, text = "Informasi Penjualan" , bg = "forest green", fg ="LightCyan2", font = "Calibri 20 bold").place(x = 550 , y = 125)
#kotak
kotak = Label(window, width = 130, height = 25 ,text = "" , bg = "LightCyan3").place(x = 200 , y = 120)

#buat label halaman
welcome = Label(window, text = "Jual Hasil Tani" , bg = "forest green", fg ="LightCyan2", font = "Calibri 20 bold").place(x = 0 , y = 30)

#buat label
barang = Label(window, text = "Nama Buah/Sayur \t\t: " , bg = "LightCyan3", fg ="forest green", font = "Calibri 15 bold").place(x = 250 , y = 200)
kuantitas = Label(window, text = "Kuantitas (kg)\t\t: " , bg = "LightCyan3", fg ="forest green", font = "Calibri 15 bold").place(x = 250 , y = 250)
harga = Label(window, text = "Harga Jual (per kg)\t\t:    Rp " , bg = "LightCyan3", fg ="forest green", font = "Calibri 15 bold").place(x = 250 , y = 300)
rekening = Label(window, text = "No. Rekening)\t\t:", bg = "LightCyan3", fg ="forest green", font = "Calibri 15 bold").place(x = 250 , y = 350)

#buat input
stringnama = StringVar()
ibar = Entry (window, width = 50, fg ="forest green", font = "Calibri 15 bold", textvariable = stringnama).place(x = 550 , y = 200)
intkuantitas = IntVar()
ikuan = Entry (window, width = 50, fg ="red", font = "Calibri 15 bold", textvariable = intkuantitas).place(x = 550 , y = 251)
intharga = IntVar()
ihar = Entry (window, width = 45, fg ="red", font = "Calibri 15 bold", textvariable = intharga).place(x = 600 , y = 301)
intrekening = IntVar()
irek = Entry (window, width = 50, fg ="red", font = "Calibri 15 bold", textvariable = intrekening).place(x = 550 , y = 351)


#buat tombol
jual = Button(window, width = 10,height = 1, command = jual, text = "Jual", bg = "forest green", fg = "LightCyan2", font = "Calibri 15 bold").place(x = 940,y = 400)
back = Button(window, width = 10,height = 1, command = window.destroy, text = "Back", bg = "black", fg = "white", font = "Calibri 10 bold").place(x = 50,y = 600)


window.mainloop()    
