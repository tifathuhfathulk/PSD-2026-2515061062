# Sistem Perhitungan Suara
## Deskripsi Singkat
Sistem Perhitungan Suara Pilkada ini dirancang untuk menghitung hasil pemilihan dari 100 pemilih terhadap tiga pasangan calon yang direpresentasikan dengan angka 1, 2, dan 3. Program menerima array berisi pilihan suara masing-masing pemilih, kemudian menggunakan fungsi sequential_search untuk menghitung berapa kali setiap nomor paslon muncul dalam array tersebut. Hasil perhitungan ditampilkan dalam bentuk tabel yang menunjukkan jumlah suara dan persentase untuk setiap paslon, diikuti penentuan pemenang secara otomatis berdasarkan suara terbanyak.


## Source Code
<img width="1920" height="1008" alt="image" src="https://github.com/user-attachments/assets/f4ef87a0-0293-45b0-a39f-d609e5b171e1" />
<img width="1920" height="1008" alt="tugas_akhir_judul3 py - judul 3 psd - Visual Studio Code 5_6_2026 1_31_18 PM" src="https://github.com/user-attachments/assets/4d1d0ee2-2e2a-4d35-b494-f67423054150" />

## Penjelasan Kode
- def sequential_search(data, n, target): untuk mendefinisikan fungsi sequential_search dengan parameter data yg merupakan daftar suara pemilih, n berupa berapa banyak pemilih, dan target yang merupakan nomor paslon yang dicari
- i = 0 mulai dari indeks ke 0
- counter = 0 mulai menghitung jumlah suaranya dari 0
- while i < n: artinya ulang terus selama penanda i masih kurang dari jumlah pemilih n
- if data[i] == target: untuk cek apakah suara pemilih ke-i sama dengan paslon target
- counter += 1 jika sura pemilih ke-i = target maka tambah 1 ke counter, counter di sini fungsinya untuk menghitung banyaknya kemunculan si target tadi
- i += 1 artinya lanjut ke indeks selanjutnya
- return counter setelah selesai iterasinya, kembalikan hasil counter tadi
- def main(): untuk mendefinisikan menu utamanya yaitu main()
- suara_pemilih = [1,2,1,2,3,1,2,2,1,3, 2,3,3,3,1,2,3,1,2,1...] artinya untuk membuat variabel suara pemilih dengan daftar suara 100 orang pemilih
- n = len(suara_pemilih) untuk menghitung jumlah pemilihnya
- print("=== SISTEM PERHITUNGAN SUARA PILKADA ===")
    print("Paslon 1: Naruto-Sasuke")
    print("Paslon 2: Nagi-Reo") 
    print("Paslon 3: Martin-James")
  untuk menampilkan nama-nama pasangan calon
- print(f"\nData suara {n} pemilih: {suara_pemilih[:10]}...") sebagai preview 10 suara pertama biar keliatan datanya
- suara = [0, 0, 0, 0]  buat kotak skor untuk 3 paslon (index 1, 2, dan 3)
- print("\n--- HASIL PERHITUNGAN ---")
    print("Paslon\tSuara\tPersentase")
    print("-"*25) untuk menampilkan hasil perhitungan suara dalam bentuk tabel
- total_suara = 0 untuk menyiapkan total semua suara (awalnya 0)
- for paslon in [1, 2, 3]: ulang tiga kali untuk paslon 1, 2, 3
- counter = sequential_search(suara_pemilih, n, paslon) untuk memanggil fungsi sequential search dan mendapat jumlah suara paslonnya
- suara[paslon] = counter untuk menulis skor ke kotak skor suatu paslon
- total_suara += counter untuk tambah ke total semua suara
- persen = (counter/n)*100
  print(f"{paslon}\t{counter}\t{persen:.1f}%") untuk menghitung hasilnya dalam
  bentuk presentase dan menampilkannya ke tabel
- paslon_nama = {1: "Naruto-Sasuke", 2: "Nagi-Reo", 3: "Martin-James"}
- pemenang = max(range(1,4), key=lambda x: suara[x]) untuk mencari pemenang dengan suara terbanyak dan presentase tertinggi
- suara_pemenang = suara[pemenang] untuk ambil skor pemenang dari kotak skor
- print(f"\nTotal suara: {total_suara}/{n}")
  print(f"Paslon Pemenang {pemenang}: {paslon_nama[pemenang]}")
  print(f"Suara: {suara_pemenang} ({(suara_pemenang/n)*100:.1f}%)")
  untuk menampilkan hasil pemilihan dan perhitungan suara tersebut dengan lengkap
 - if __name__ == "__main__":
    main() memanggil fungsi main() untuk menjalankan programnya.

## Penjelasan Output
<img width="1920" height="1008" alt="image" src="https://github.com/user-attachments/assets/ab2f110e-6611-4c6a-997c-7597955b513b" />

- Pada outputnya itu menampilkan siapa saja nama-nama pasangan calonnya beserta nomor urut.
- Kemudian ada Data 90 pemilih dengan menampilkan 10 suara pertama sebagai preview yang merupakan hasil dari kode print(f"\nData suara {n} pemilih: {suara_pemilih[:10]}...") ini.
- Kemudian ditampilkan juga tabel hasil perhitungan berupa nomor urut paslon, jumlah suara yang didapatkan, dan presentasenya.
- Kemudian menampilkan hasil perhitungan dengan menampilkan nama pemenang dan jumlah suara yang didapatkan.
  
## Link YouTube
