# Program Pengurutan High Score 

## Deskrpsi Singkat
Sistem pengurutan skor tertinggi ini berfungsi untuk menampilkan daftar pemain dalam game dari skor paling besar ke paling kecil, sehingga pemain dapat melihat ranking atau peringkat siapa yang memiliki skor tertinggi. Proses ini membantu menata data sehingga tampil rapi dan mudah dibaca, misalnya untuk menampilkan high score di menu utama atau hall of fame. Sistem ini menggunakan algoritma bubble sort karena cara kerjanya sederhana dan mudah dipahami, yaitu dengan terus membandingkan dua skor berdekatan dan menukarnya jika skor di depan lebih kecil, sehingga skor besar “naik ke atas” secara bertahap. Meskipun tidak secepat algoritma lain, bubble sort cocok untuk pemula dan data yang masih sedikit, sehingga sangat pas untuk contoh sistem ranking skor dalam game sederhana.

## Source Code
<img width="1920" height="1008" alt="● tugas_akhir_judul2 py - Visual Studio Code 4_27_2026 7_55_08 PM" src="https://github.com/user-attachments/assets/5d068e9d-1a1a-4a92-8d9b-104237f479f2" />
<img width="1920" height="1008" alt="● tugas_akhir_judul2 py - Visual Studio Code 4_27_2026 7_55_23 PM" src="https://github.com/user-attachments/assets/a4617cc8-34aa-4212-bafa-abfc589457f5" />

## Penjelasan Source Code
- def tukar(arr, i, j): untuk mendefinisikan fungsi bernama tukar dengan parameter arr berupa list yang berisi skor, i merupakan posisi angka pertama, dan j merupakan posisi angka kedua
- temp = arr[i] untuk 
