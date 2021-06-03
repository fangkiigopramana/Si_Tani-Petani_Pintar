from tkinter import * 
from tkinter import ttk

def apel():
    from fileTanamBuah import apel

def durian():
    from fileTanamBuah import durian

def jambuAir():
    from fileTanamBuah import jambuAir

def pisang():
    from fileTanamBuah import pisang

def mangga():
    from fileTanamBuah import mangga

window = Tk()  
window.title("Si-Tani (Petani Pintar")
window.configure(bg="LightCyan2")
window.state("zoomed")

#buat label halaman
welcome = Label(window, text = "Tanam Buah" , bg = "forest green", fg ="LightCyan2", font = "Calibri 20 bold").place(x = 0 , y = 30)

#buat tombol "lihat"
apel = Button(window, command = apel, text = "Buah Apel", bg = "forest green", fg = "LightCyan2", font = "Calibri 12 bold").place(x = 230,y = 300)
durian = Button(window, command = durian, text = "Buah Durian", bg = "forest green", fg = "LightCyan2", font = "Calibri 12 bold").place(x = 430,y = 300)
jambuAir = Button(window, command = jambuAir, text = "Buah Jambu Air", bg = "forest green", fg = "LightCyan2", font = "Calibri 12 bold").place(x = 630,y = 300)
pisang = Button(window, command = pisang, text = "Buah Pisang", bg = "forest green", fg = "LightCyan2", font = "Calibri 12 bold").place(x = 830,y = 300)
mangga = Button(window, command = mangga, text = "Buah Mangga", bg = "forest green", fg = "LightCyan2", font = "Calibri 12 bold").place(x = 1030,y = 300)
#buat tombol
back = Button(window, width = 10,height = 2, command = window.destroy, text = "Back", bg = "black", fg = "white", font = "Calibri 10 bold").place(x = 50,y = 600)

window.mainloop()    