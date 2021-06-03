from tkinter import * 
from tkinter import ttk,messagebox 

window = Tk()  
window.title("Si-Tani (Petani Pintar")
window.configure(bg="LightCyan2")
window.state("zoomed")

#buat fungsi
def tanamBuah():
    from tugasAkhir import tanamBuah
def tanamSayur():
    from tugasAkhir import tanamSayur   
def kursSayurBuah():
    from tugasAkhir import  kursSayurBuah
def jualHasilTani():
    from tugasAkhir import jualHasilTani 

#buat label halaman
welcome = Label(window, text = "Selamat datang," , bg = "forest green", fg ="LightCyan2", font = "Calibri 20 bold").place(x = 0 , y = 30)

#buat caption
caption = Label(window, text = ".Kebanggaanku adalah terlahir dari seorang petani.", fg = "LightCyan4",bg = "LightCyan2", font = "Calibri 15 italic", justify="left").place(x = 500, y = 100)

#buat menu button 
menu1 = Button(window, width = 20, height = 5, command = tanamBuah, text="TANAM BUAH",fg = "green", font = "Calibri 15 bold").place(x=50,y=300)
menu2 = Button(window, width = 20, height = 5, command = tanamSayur, text="TANAM SAYUR",bg = "green", fg = "white", font = "Calibri 15 bold").place(x=400,y=300)
menu3 = Button(window, width = 20,height = 5, command = kursSayurBuah, text="KURS\nSAYUR & BUAH", bg = "white", fg = "green", font = "Calibri 15 bold").place(x=750,y=300)
menu4 = Button(window, width = 20,height = 5, command = jualHasilTani, text="JUAL\nHASIL TANI", fg = "white", bg = "green", font = "Calibri 15 bold").place(x=1100,y=300)
back = Button(window, width = 10,height = 2, command = window.destroy, text = "Back", bg = "black", fg = "white", font = "Calibri 10 bold").place(x = 50,y = 600)

window.mainloop()    