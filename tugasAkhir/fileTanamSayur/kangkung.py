from tkinter import *
from tkinter import ttk 
keterangan = """    
    Nama Umum
    >> Kangkung
    Nama latin
    >> Ipomoea aquatica
    Asal
    >> India
    Prosedur Menanam:
    Alat dan bahan
    - Bakul anyam
    - Pot/polybag
    - Tanah dan kompos
    - Arang sekam

    Cara menanam
    1. Memilih bibit unggul.
    2. Siapkan tanah dan kompos, dan biarkan semalaman.
    3. Tabur bibit unggul dan tutup menggunakan jaring-jaring.
    4. Lakukan penyiraman dua kali sehari. Biasanya, kecambah akan tumbuh dalam waktu 5-7 hari.
    5. Pindahkan kecambah tersebut ke pot/polybag.
    6. Siapkan pot/polybag, yang memiliki lubang di bawahnya. Lalu masukan tanah dan kompos, dengan perbandingan 2:1 dan biarkan semalaman.
    7. Pindahkan kecambah ke dalam pot tersebut. Setiap pot bisa diisi 2 bibit yang sudah berkecambah.
    8. Lakukan penyiraman dua kali sehari, pagi dan siang secara rutin.
    9. Jangan terlalu banyak menyiram air, karena ditakutkan busuk.
    10. Jangan lupa berikan pupuk organik, agar hasil lebih maksimal.
    11. Untuk panen, biasanya ketika kangkung sudah berusia 25-39 hari.
    """

window = Tk()  
window.title("Si-Tani (Petani Pintar")
window.configure(bg="LightCyan2")
window.state("zoomed")

kotak = Label(window, width = 150, height = 42 ,text = "" , bg = "LightCyan3").place(x = 200 , y = 20)

#buat isi
konten = Label(window, text = keterangan , bg = "LightCyan3", fg ="black", font = "Calibri 12 bold", justify = "left").place(x = 200 , y = 20)

#buat label halaman
welcome = Label(window, text = "Kangkung" , bg = "forest green", fg ="LightCyan2", font = "Calibri 20 bold").place(x = 0 , y = 30)

#buat tombol
back = Button(window, width = 10,height = 2, command = window.destroy, text = "Back", bg = "black", fg = "white", font = "Calibri 10 bold").place(x = 50,y = 600)

window.mainloop()    