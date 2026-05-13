# Sistem Waiting List Restaurant

## Deskripsi Singkat
Waiting List Restoran adalah daftar tunggu yang digunakan untuk mengatur antrian pelanggan saat semua meja sudah penuh. Tujuannya adalah untuk memudahkan restoran untuk menyiapkan pesanan sesuai dengan antrian pelanggan, sehingga tidak terjadi kekacawan atau keributan karena pelanggan yang datang duluan tidak dilayani lebih dulu. Dalam programnya, queue linked list dipilih karena bekerja seperti antrian sungguhan dengan aturan FIFO (pertama masuk, pertama keluar), sehingga pelanggan pertama yang datang dilayani duluan. Struktur ini juga fleksibel, bisa menambah atau menghapus pelanggan dengan cepat tanpa batas ukuran seperti array biasa, membuatnya sangat cocok untuk situasi restoran yang sibuk.
## Source Code
<img width="1920" height="1008" alt="image" src="https://github.com/user-attachments/assets/c2099c42-aa22-472d-80c1-e7650f765aaa" />
<img width="1920" height="1008" alt="image" src="https://github.com/user-attachments/assets/48d61039-e5e7-4000-81c7-b1bc0f49010e" />
<img width="1920" height="1008" alt="image" src="https://github.com/user-attachments/assets/677c03cf-90b2-4aa9-b229-3d0b1c201253" />
<img width="1920" height="1008" alt="image" src="https://github.com/user-attachments/assets/84cdbfac-4a69-491d-81c4-38e5be928e61" />

## Penjelasan Kode
- class Node: ini berfungsi untuk mendefinisikan sebuah blueprint atau tipe data bernama Node.
- def __ init__(self, data): ini berfungsi untuk mendefinisikan fungsi konstruktor (fungsi yang otomatis dipanggil saat kita membuat Node baru). Parameter di dalam kurung (data) adalah nilai yang ingin kita simpan di Node itu.
- self.data = data Baris ini menyimpan nilai yang diberikan (data) ke dalam Node yang baru dibuat, sehingga Node tersebut "mengingat" data itu.
- self.next = None Baris ini membuat penunjuk (link) ke Node berikutnya dan mengisinya dengan None (kosong) pada awalnya, artinya sekarang Node ini belum terhubung ke Node lain.
- class QueueLinkedList: Ini mendefinisikan blueprint untuk antrian (queue) yang dibangun dari Node-node tadi.
- def _init_(self): Konstruktor untuk objek QueueLinkedList, dipanggil otomatis saat membuat antrian baru.
- self.front_ptr = None Ini menyimpan alamat (penunjuk) ke Node paling depan (depan antrian). Di awal dibuat None karena antrian masih kosong.
- self.rear_ptr = None Ini menyimpan alamat ke Node paling belakang (bagian akhir antrian). Juga None di awal karena kosong.
- def is_empty(self): mendefinisikan fungsi is_empty untuk mengecek apakah antrian kosong atau tidak
- return self.front_ptr is None Mengembalikan nilai True jika front_ptr kosong (artinya antrian kosong), False jika ada isi.
- def enqueue(self, x): Fungsi untuk menambahkan elemen baru ke belakang antrian; parameter x adalah data yang ingin ditambahkan (dalam hal ini adalah nama pelanggan).
- new_node = Node(x) untuk membuat Node baru yang menyimpan data x.
- if self.is_empty(): untuk memeriksa apakah antrian saat ini kosong.
- self.front_ptr = new_node Jika kosong, Node baru menjadi Front (depan) karena hanya ada satu elemen.
- self.rear_ptr = new_node Jika kosong, Node baru juga menjadi Rear (belakang).
- else: Jika antrian tidak kosong, jalankan langkah berikutnya.
- self.rear_ptr.next = new_node untuk menghubungkan Node yang sekarang di belakang ke Node baru; artinya Node lama sekarang menunjuk ke Node baru.
- self.rear_ptr = new_node untuk memperbarui penunjuk belakang agar sekarang menunjuk ke Node baru (karena Node baru adalah yang paling terakhir).
- print(f"Pelanggan {x} berhasil ditambahkan") untuk menampilkan pesan konfirmasi bahwa pelanggan berhasil ditambahkan ke antrian.
- def dequeue(self): Fungsi untuk menghapus elemen yang ada di depan antrian (yang datang paling dulu). dengan parameter self
- if self.is_empty(): untuk mengecek dulu apakah antrian kosong.
- print("Antrian kosong") Jika kosong, beri tahu pengguna bahwa antrian kosong
- return untuk keluar dari fungsi karena tidak ada yang dihapus.
- temp = self.front_ptr untuk menyimpan Node depan ke variabel sementara untuk referensi (misal untuk tampilkan datanya sebelum dihapus).
- print(f"Antrian {temp.data} berhasil dihapus") untuk menampilkan data dari Node yang dihapus (misal nama pelanggan yang keluar dari antrian).
- self.front_ptr = self.front_ptr.next untuk menggeser penunjuk depan ke Node berikutnya, ini secara logis menghapus Node depan dari antrian.
- if self.front_ptr is None: Jika setelah penggeseran, front_ptr jadi None (berarti antrian jadi kosong).
- self.rear_ptr = None Maka juga ubah rear_ptr jadi None supaya konsisten (tidak ada elemen sama sekali).
- def peek(self): Fungsi untuk melihat siapa yang ada di depan antrian tanpa menghapusnya.
- if self.is_empty(): untuk cek apakah antrian kosong.
- print("Antrian kosong") Jika kosong, beri tahu pengguna.
- return Keluar dari fungsi karena tidak ada data untuk ditampilkan.
- print(f"Antrian terdepan, yaitu atas nama : {self.front_ptr.data}") untuk menampilkan nama pelanggan yang berada di depan antrian.
- def display(self): Fungsi untuk menampilkan seluruh isi antrian, dari depan ke belakang.
- if self.is_empty(): untuk cek apakah antrian kosong.
- print("Antrian kosong") jika antrian kosong maka akan menampilkan antrian kosong
- return untuk keluar dari fungsi
- print("Seluruh Antirian Saat ini: ", end="") untuk mencetak judul daftar antrian, dan end="" agar tidak membuat baris baru langsung.
- current = self.front_ptr untuk membuat variabel bantu current yang mulai dari depan antrian.
- while current is not None: Perulangan yang berjalan selama masih ada Node (sampai akhir antrian).
- print(current.data, end=" ") untuk mencetak data Node saat ini (misal nama pelanggan) di satu baris, dipisah spasi.
- current = current.next untuk pindah ke Node berikutnya.
- print() Setelah selesai looping, cetak baris baru untuk rapikan tampilan.
- def main(): untuk mendefinisikan menu utamanya yaitu main()
- queue = QueueLinkedList() untuk membuat sebuah objek antrian baru bernama queue.
- pilih = 0 untuk inisialisasi variabel pilihan menu.
- while pilih != 5: merupakan loop yang terus berjalan sampai pengguna memilih opsi 5 (keluar).
- print("\\n=== Waiting List Restaurant ===")
- print("1. Menambahkan Antrian")
- print("2. Menghapus Antrian")
- print("3. Melihat Antrian Terdepan")
- print("4. Melihat Seluruh Data Antrian")
- print("5. Keluar Pogram") untuk menampilkan seluruh menu dari 1-5
- try: untuk mencoba/memulai blok yang mencoba menjalankan kode yang mungkin menimbulkan error.
- pilih = int(input("Pilih: ")) untuk membaca input dari pengguna, lalu mengubahnya ke bilangan bulat, angka ini menentukan pilihan menu.
- except ValueError: jika input bukan angka maka akan menampilkan ValueError ini
- print("Input tidak valid!") program akan memberitahu bahwa input tidak valid
- continue Melanjutkan kembali ke awal loop tanpa menjalankan kode pilihan selanjutnya.
- if pilih == 1: jika pengguna memilih menu 1
- try program akan menjalankan kode menu 1
- val = str(input("Masukkan Nama Pelanggan: ")) untuk meminta pengguna memasukkan nama pelanggan, simpan sebagai string.
- queue.enqueue(val) Panggil fungsi enqueue untuk menambahkan nama itu ke antrian.
- except ValueError: jika terjadi kesalahan input
- print("Input tidak valid!") maka akan menampilkan input tidak valid
- elif pilih == 2: jika memilih menu 2
- queue.dequeue() Panggil fungsi dequeue untuk menghapus pelanggan depan.
- elif pilih == 3: jika memilih menu 3
- queue.peek() Panggil fungsi peek untuk menampilkan nama depan. 
- elif pilih == 4: jika memilih menu 4
- queue.display() Panggil fungsi display untuk mencetak seluruh antrian.
- elif pilih == 5: jika memilih menu 5
- while not queue.is_empty(): Selama antrian tidak kosong
- queue.dequeue() maka hapus semua elemen satu per satu (membersihkan antrian sebelum keluar).
- print("Program selesai.") tampilkan pesan program selesai
- else: Jika input angka tapi bukan 1-5
- print("Pilihan tidak valid!") maka beri tahu pengguna pilihannya tidak tersedia. 
- if _name_ == "_main_":
-  main() panggil fungsi main() untuk menjalankan program.

## Penjelasan Output
<img width="1920" height="1008" alt="image" src="https://github.com/user-attachments/assets/57f6fbe0-1ee6-4661-b403-5303849e4cf3" />
<img width="1920" height="1008" alt="image" src="https://github.com/user-attachments/assets/98a60d09-2ff3-420a-b5b0-178a80ce4bd9" />

- Pada outputnya jika kalian memilih menu 1, maka akan diminta untuk menampilkan nama pelanggan untuk ditambahkan ke dalam antrian, nama akan dimasukkan ke antrian belakang.
- Jika memilih menu 2, maka program akan menghapus antrian dari depan jika sudah selesai dilayani, pada contoh ini saya mengapus antrian terdepan yaitu Aliyah.
- Jika memilih menu 3, maka program akan menampilkan siapa pelanggan terdepan saat ini yang harus dilayani.
- Jika memilih menu 4, maka program akan menampilkan seluruh antrian saat ini.
- Jika memilih menu 5 maka program akan selesai, dan jika masih ada antrian di dalam program maka antrian tersbut akan otomatis terhapus dan dianggap sudah dilayani.

## Link YouTube
- https://youtu.be/5ECJB3fNTt0
