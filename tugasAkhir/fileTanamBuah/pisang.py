from tkinter import *
from tkinter import ttk 
keterangan = """    
    Nama Umum
    >> Pisang
    Nama latin
    >> Musa
    Asal     
    >> Asia Tenggara
    Prosedur Menanam:
    Alat & Bahan
		a. Bibit pohon pisang
        b. Lahan yang lembab
        c. Cetok
        d. Air
        
	Cara menanam
    	a. Siapkan sebuah lubang berukuran minimal 30 cm dan kedalaman 30 cm. 
        b. Masukkanlah bibit pisang ke dalam tanah lalu siram dengan air dalam jumlah yang banyak.
        c. Apabila tanaman pisang Anda mulai tumbuh, potong dahan yang mati untuk memastikan pertumbuhannya bisa terus berlangsung.
        d. Tanaman pisang membutuhkan waktu sedikitnya 3-4 bulan hingga bisa berbuah. 
        e. Apabila sudah berbuah, maka potong jantung pisang untuk memacu pertumbuhan buah dari pisang.
        f. Lindungilah buah pisang yang masih berwarna hijau dari hama dengan menggunakan kantong plastik. 
        g. Segeralah panen buah pisang apabila berwarna kekuningan serta bunga dan daun-daunnya mulai mati dan mengering. """

window = Tk()  
window.title("Si-Tani (Petani Pintar")
window.configure(bg="LightCyan2")
window.state("zoomed")

kotak = Label(window, width = 150, height = 42 ,text = "" , bg = "LightCyan3").place(x = 200 , y = 20)

#buat isi
konten = Label(window, text = keterangan , bg = "LightCyan3", fg ="black", font = "Calibri 12 bold", justify = "left").place(x = 200 , y = 20)

#buat label halaman
welcome = Label(window, text = " Pisang " , bg = "forest green", fg ="LightCyan2", font = "Calibri 20 bold").place(x = 0 , y = 30)

#buat tombol
back = Button(window, width = 10,height = 2, command = window.destroy, text = "Back", bg = "black", fg = "white", font = "Calibri 10 bold").place(x = 50,y = 600)

window.mainloop()    