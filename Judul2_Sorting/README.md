# Program Pengurutan High Score 

## Deskrpsi Singkat
Sistem pengurutan skor tertinggi ini berfungsi untuk menampilkan daftar pemain dalam game dari skor paling besar ke paling kecil, sehingga pemain dapat melihat ranking atau peringkat siapa yang memiliki skor tertinggi. Proses ini membantu menata data sehingga tampil rapi dan mudah dibaca, misalnya untuk menampilkan high score di menu utama atau hall of fame. Sistem ini menggunakan algoritma bubble sort karena cara kerjanya sederhana dan mudah dipahami, yaitu dengan terus membandingkan dua skor berdekatan dan menukarnya jika skor di depan lebih kecil, sehingga skor besar “naik ke atas” secara bertahap. Meskipun tidak secepat algoritma lain, bubble sort cocok untuk pemula dan data yang masih sedikit, sehingga sangat pas untuk contoh sistem ranking skor dalam game sederhana.

## Source Code
<img width="1920" height="1008" alt="● tugas_akhir_judul2 py - Visual Studio Code 4_27_2026 7_55_08 PM" src="https://github.com/user-attachments/assets/5d068e9d-1a1a-4a92-8d9b-104237f479f2" />
<img width="1920" height="1008" alt="● tugas_akhir_judul2 py - Visual Studio Code 4_27_2026 7_55_23 PM" src="https://github.com/user-attachments/assets/a4617cc8-34aa-4212-bafa-abfc589457f5" />

## Penjelasan Source Code
- def tukar(arr, i, j): untuk mendefinisikan fungsi bernama tukar dengan parameter arr berupa list yang berisi skor, i merupakan posisi angka pertama, dan j merupakan posisi angka kedua
- temp = arr[i] sebagai tempat sementara bernama temp, lalu simpan angka yang ada di posisi i di sana.
​- arr[i] = arr[j] maksudnya itu ambil angka di posisi j, lalu pasang ke posisi i. Jadi posisi i sekarang berisi angka j
- arr[j] = temp maksudnya ambil angka yang tadi disimpan di temp (aslinya dari posisi i), lalu pasang ke posisi j.
- def bubble_sort_desc(arr, n): untuk membuat resep bernama bubble_sort_desc (descending = dari besar ke kecil) dengan n= jumlah elemen.
- for i in range(n - 1): maksudnya itu kalau total ada 5 skor, n - 1 = 4, jadi akan ada 4 putaran besar.
- for j in range(n - i - 1): maksudnya dalam satu putaran besar, kita bandingkan pasangan skor berdekatan atau yang bersebelahan.
- n - i - 1 untuk membuat pada setiap putaran, kita tidak perlu lagi memeriksa angka‑angka yang sudah sesuai urutan di belakang.
- if arr[j] < arr[j + 1]: untuk memeriksa apakah angka di posisi j lebih kecil dari angka di posisi j + 1? Kalau iya, artinya skor kecil dulu, skor besar belakang
- tukar(arr, j, j + 1) maksudnya Kalau kondisi di atas benar, tukar posisi j dan j+1 supaya skor besar berada di depan.

- def main(): untuk mendefinisikan fungsi main sebagai bagian utama program
- try: untuk menjalankan program
- n = int(input("Masukkan jumlah pemain: ")) maksudnya user dapat menginputkan berapa jumlah pemainnya dalam bentuk integer
- if n <= 0: untuk cek apakah pemain 0 atau negatif? Kalau iya maka tidak masuk akal untuk game
- print("Jumlah pemain harus lebih dari 0!") ini akan muncul ketika user menginputkan angka 0 atau negatif
- return untuk menghentiukan fungsi main di sana
- except ValueError:
- print("Input tidak valid!") ini akan muncul ketika user menginputkan selain angka, misal berupa huruf ataupun simbol
- return

- skor = [] untuk membuat “daftar kosong” bernama skor yang nanti akan diisi angka skor pemain
- nama = []  untuk membuat “daftar kosong” bernama nama yang nanti akan diisi angka nama pemain
- print("Masukkan data pemain (nama skor):") untuk memberikan petunjuk kepada user untuk mengetikkan dalam format "nama skor"
- for i in range(n): untuk mengulangi sebanyak jumlah pemain yang dimasukkan user
- while True: Ini merupakan “loop tak terbatas” sampai user mengetik dengan format benar. Jika salah, program akan ulang lagi minta input.
- try: untuk coba proses input. Kalau ada error, akan ditangkap di exceptValueError 
- data = input().strip().split() setelah user mengetikkan satu baris, spasi di awal dan di akhir akan dihilangkan dan dipecah jadi list
- if len(data) != 2: untuk cek apakah inputnya persis dua bagian, yaitu nama dan skor. Kalau bukan 2 bagian, format salah.
- print("Format: nama skor (contoh: Ali 1500)") untuk meminta user mengetikkan sesuai format yang benar
- continue untuk  lanjut ke putaran while berikutnya
- nama_pemain = data[0] untuk ambil bagian pertama (data[0]) itu adalah nama pemain.
- nilai_skor = int(data[1]) untuk ambil bagian kedua (data[1]) dan ubah ke angka itu adalah skor.
- nama.append(nama_pemain) untuk masukkan nama pemain ke daftar nama
- skor.append(nilai_skor) untuk masukkan skor pemain ke daftar skor
- break Jika semua sampai sini tanpa error, hentikan loop while dan lanjut ke pemain berikutnya.
- except ValueError:
- print("Skor harus berupa angka!") ini akan muncul ketika user menginputkan selain angka
- print("\nSkor sebelum diurutkan:") untuk mencetak judulnya, \n sebagai new line
- for i in range(n): maksudnya ulangi untuk setiap pemain (0 sampai n-1).
- print(f"{i+1}. {nama[i]} | Skor: {skor[i]}") untuk menampilkan urutan i+1, nama pemain, dan skor
-  bubble_sort_desc(skor, n) untuk memanggil fungsi bubble_sort_desc tadi
-  print("\nRanking skor tertinggi (High Score):") untuk cetak judul high score
-  for i in range(n): untuk mengulangi untuk setiap pemain.
-  print(f"{i+1}. Skor: {skor[i]}") untuk menampilkan posisi ranking (1, 2, 3, …) dan skor yang sudah terurut.Skor tertinggi akan muncul di ranking 1.
- main() untuk memanggil fungsi main tadi

## Penjelasan Output Program
<img width="1600" height="840" alt="WhatsApp Image 2026-04-27 at 22 17 12" src="https://github.com/user-attachments/assets/bdb41b00-ad7e-446f-9461-d55b52c0a45b" />

- user diminta memasukkan jumlah pemain dalam bentuk integer, jumlah pemain ini akan digunakan umtuk menentukan berapa kali terjadi perulangannya.
- kemudian user diminta memasukkan data pemain dengan format "nama skor" sebanyak jumlah pemain tadi. Apabila user salah format dalam penginputan data maka program akan mengulangi lagi meminta input.
- Setelah itu sistem akan menampilkan data yang masih belum terurut tadi sesuai dengan urutan inputan user
- Kemudian sistem akan menampilkan ranking tertingi(high score), yang mana dalam pengurutan data tersebut menggunakan fungsi bubble_sort_desc tadi

## Link Video YouTube
