from tkinter import * 
from tkinter import ttk

#main
window = Tk()  
window.title("Si-Tani (Petani Pintar")
window.configure(bg="LightCyan2")
window.state("zoomed")

#buat class Tabel
class Table:
    def __init__ (self,window):
        for i in range (total_rows):
            for j in range (total_columns):
                self.e = Entry (window, width = 20, fg = "black", justify = "center",font = ("Calibri", 18,"bold"))
                self.e.grid (row = i, column = j)
                self.e.insert(END,lst[i][j])

lst = [("","","","",""),
       ("","","","",""),
       ("","","","",""),
       ("","","","",""),
       ("","","","",""),
       ("No.","Nama Buah","Harga (per kg)","Nama Sayur","Harga (per kg)"),
       ("1.", "Apel","Rp 17.500","Tomat","Rp 11.000" ),
       ("2.", "Durian", "Rp 50.000","Cabai","Rp 20.000" ),
       ("3.", "Jambu Air", "Rp 30.000" ,"Kangkung","Rp 10.000" ),
       ("4.", "Pisang","Rp 20.000" ,"Mentimun","Rp 10.000" ),
       ("5.", "Mangga", "Rp 15.000","Terong","Rp 14.000" )]

total_rows = len(lst)
total_columns = len(lst[0])

t = Table(window)

Label(window, width = 174, text = " \n\n\n\n\n\n\n\n\n\n", bg = "LightCyan2").place(x = 0 , y = 0)
#buat label halaman
welcome = Label(window, text = "Kurs Sayur & Buah" , bg = "forest green", fg ="LightCyan2", font = "Calibri 20 bold").place(x = 0 , y = 30)
#buat tombol
back = Button(window, width = 10,height = 2, command = window.destroy, text = "Back", bg = "black", fg = "white", font = "Calibri 10 bold").place(x = 50,y = 600)

window.mainloop()    