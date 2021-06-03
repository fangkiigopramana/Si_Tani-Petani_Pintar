from tkinter import * 
from tkinter import ttk
def halamanUtama ():
    from tugasAkhir import halamanFitur
window = Tk()
#window.geometry("300x200")
window.title("Si-Tani (Petani Pintar)")
window.configure(bg="LightCyan2")
window.state("zoomed")

#buat label
S = Label(window, text = " S.t ", bg = "forest green", fg ="LightCyan2", font = "TimesNewRoman 30 bold", justify = "right").place(x = 500 , y = 117)
welcome = Label(window, text = "Si - Tani ", bg = "LightCyan2", fg ="forest green", font = "Calibri 50 bold").place(x = 600 , y = 99)
pesan = Label(window, text = "Pertanian merupakan salah satu sektor ekonomi yang berperan penting dalam pertumbuhan ekonomi.\nAtas dasar itu, aplikasi ini dibuat untuk menyejahterahkan petani dan membantu peningkatan ekonomi Indonesia.", justify ="center", font = "Calibri 15 italic ", bg = "LightCyan2",fg = "LightCyan4").place(x = 200, y = 280)

#buat button
masuk = Button(window, command = halamanUtama, text="Masuk",bg = "forest green", fg = "LightCyan2", font = "Calibri 20 bold ").place(x = 600,y = 500)
label = Label(window, text = "Silahkan Klik Masuk", fg = "LightCyan4", bg = "LightCyan2", font = "Calibri 15").place(x = 560 , y = 570)
window.mainloop()    