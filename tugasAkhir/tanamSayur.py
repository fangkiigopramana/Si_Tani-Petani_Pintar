from tkinter import * 
from tkinter import ttk

from tkinter import * 
from tkinter import ttk

def tomat():
    from fileTanamSayur import tomat

def cabai():
    from fileTanamSayur import cabai

def kangkung():
    from fileTanamSayur import kangkung

def mentimun():
    from fileTanamSayur import mentimun

def terong():
    from fileTanamSayur import terong

window = Tk()  
window.title("Si-Tani (Petani Pintar")
window.configure(bg="LightCyan2")
window.state("zoomed")

#buat label halaman
welcome = Label(window, text = "Tanam Sayur" , bg = "forest green", fg ="LightCyan2", font = "Calibri 20 bold").place(x = 0 , y = 30)

#buat tombol "lihat"
Button(window, command = tomat, text = "Sayur Tomat", bg = "forest green", fg = "LightCyan2", font = "Calibri 12 bold").place(x = 230,y = 300)
Button(window, command = cabai, text = "Sayur Cabai", bg = "forest green", fg = "LightCyan2", font = "Calibri 12 bold").place(x = 430,y = 300)
Button(window, command = kangkung, text = "Sayur Kangkung", bg = "forest green", fg = "LightCyan2", font = "Calibri 12 bold").place(x = 630,y = 300)
Button(window, command = mentimun, text = "Sayur Mentimun", bg = "forest green", fg = "LightCyan2", font = "Calibri 12 bold").place(x = 830,y = 300)
Button(window, command = terong, text = "Sayur Terong", bg = "forest green", fg = "LightCyan2", font = "Calibri 12 bold").place(x = 1030,y = 300)
#buat tombol
back = Button(window, width = 10,height = 2, command = window.destroy, text = "Back", bg = "black", fg = "white", font = "Calibri 10 bold").place(x = 50,y = 600)

window.mainloop()    