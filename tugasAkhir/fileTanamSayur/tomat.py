from tkinter import *
from tkinter import ttk 
keterangan = """
    Nama Umum
    >> Tomat
    Nama latin
    >> Solanum lycopersicum
    Asal
    >> Amerika Selatan
    Prosedur Menanam:
    1. Menyiapkan pot atau polibag
        a. Untuk ukuran pot atau polibag dapat disesuaikan dengan kebutuhan ya.
    2. Menyiapkan media tanam
        a. Media tanam dapat dibuat dari kombinasi tanah, arang sekam, dan kompos dengan perbandingan 2:1:1.
        b. Media tanam tomat dapat dibuat beberapa hari sebelum ditanami agar mineral dalam kompos dapat menyatu dengan tanah.
        c. Upayakan media tanam memiliki pH 5.5 - 7, serta memiliki tingkat kesuburan yang tinggi agar pertumbuhan tomat tidak terhambat.
    3. Memilih benih tomat
        a. Dalam memilih benih tomat, perlu menentukan terlebih dahulu jenis tomat apa yang hendak ditanam.
    4. Menyemai benih tomat
        a. Semaikan benih tersebut pada media semai yang dapat terdiri dari bedengan-bedengan. 
        b. Usahakan menempatkan media semai pada tempat yang tidak terkena sinar matahari dan hujan secara langsung.
        c. Siram media semai secara teratur agar tetap dalam kondisi lembap. Dengan demikian, benih akan cepat tumbuh.
        d. Setelah bibit berusia 14 hari, maka Anda dapat memberikan pupuk untuk merangsang pertumbuhan bibit.
    5. Proses penanaman dan perawatan tanaman tomat
        a. Cara pencabutan bibit dari media semai perlu dilakukan secara perlahan agar akar bibit tomat tidak putus. 
        b. Selanjutnya tanah yang digunakan sebagai media semai dapat ikut ditanam pada pot atau polybag yang baru.
        d. Setelah bibit tomat dipindahkan, Anda perlu memberikan perawatan teratur untuk menjaga tumbuh kembang tomat tersebut. 
        e. Untuk beberapa hari pertama, Anda perlu melakukan menyiram secara rutin 2 hari sekali saja. 
        g. Anda juga perlu memberikan tongkat atau kayu penyangga untuk tomat agar dapat tumbuh secara tegak.
        h. Anda perlu memberikan tambahan nutrisi untuk tanaman tomat dengan pupuk kompos selama satu minggu setelah pemindahan bibit. 
        i. Jika tanaman tomat terserang penyakit, segeralah untuk mencabutnya atau memberi pertisida agar tidak sampai menulari pohon tomat lainnya. 
    6. Masa panen
        a. Masa panen tomat terbilang cukup cepat, sebab dalam jangka waktu tidak sampai 100 hari sudah dapat memanen tomat-tomat yang ditanam. 
        b. Ciri yang menandakan tomat siap dipanen adalah perubahan warnanya yang awalnya hijau menjadi agak kekuning-kuningan."""

window = Tk()  
window.title("Si-Tani (Petani Pintar")
window.configure(bg="LightCyan2")
window.state("zoomed")

kotak = Label(window, width = 150, height = 42 ,text = "" , bg = "LightCyan3").place(x = 200 , y = 20)

#buat isi
konten = Label(window, text = keterangan , bg = "LightCyan3", fg ="black", font = "Calibri 12 bold", justify = "left").place(x = 200 , y = 20)

#buat label halaman
welcome = Label(window, text = "Tomat" , bg = "forest green", fg ="LightCyan2", font = "Calibri 20 bold").place(x = 0 , y = 30)

#buat tombol
back = Button(window, width = 10,height = 2, command = window.destroy, text = "Back", bg = "black", fg = "white", font = "Calibri 10 bold").place(x = 50,y = 600)

window.mainloop()    