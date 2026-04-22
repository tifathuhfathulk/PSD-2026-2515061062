# Program Inventaris Barang di Toko

## Deskripsi Singkat
Program inventaris barang toko merupakan sebuah sistem sederhana yang dirancang untuk membantu pengelolaan data barang menggunakan struktur data list. Dalam implementasinya, setiap barang yang ada di toko disimpan dalam sebuah list yang berisi informasi penting berupa nama barang. Dengan menggunakan list, program dapat dengan mudah melakukan berbagai operasi seperti menambah data barang baru, menampilkan seluruh daftar barang, mencari posisi barang dalam list, hingga menghapus barang yang sudah tidak tersedia. Struktur list dipilih karena sifatnya yang dinamis, sehingga memudahkan pengelolaan data yang dapat berubah sewaktu-waktu sesuai kondisi stok di toko.
Program inventaris barang ini dibuat dengan tujuan untuk meningkatkan efisiensi dan ketertiban dalam pengelolaan stok barang di toko. Tanpa sistem yang terorganisir, pemilik toko akan kesulitan memantau jumlah barang, berisiko mengalami kehabisan stok, atau bahkan terjadi kesalahan pencatatan. Dengan adanya program ini, proses pencatatan menjadi  lebih cepat, akurat, dan mudah diakses.

## Kode Program
<img width="1800" height="1008" alt="● tugas_akhir_judul1 py - Visual Studio Code 4_22_2026 6_02_31 PM" src="https://github.com/user-attachments/assets/6d7146dd-6855-4c94-96cc-0615b2670720" />
<img width="1800" height="1008" alt="● tugas_akhir_judul1 py - Visual Studio Code 4_22_2026 6_02_48 PM" src="https://github.com/user-attachments/assets/b4c4a32c-8efb-4a60-ae6e-7617a79a3781" />
<img width="1800" height="1008" alt="● tugas_akhir_judul1 py - Visual Studio Code 4_22_2026 6_03_00 PM" src="https://github.com/user-attachments/assets/b327b456-5430-45f1-bc0b-1eaeccadd2f3" />

## Penjelasan Kode Program
- inventory = []
membuat variabel global inventory berupa list kosong []. List ini akan menyimpan semua nama barang.
- def menu():
mendefinisikan fungsi bernama menu (tanpa parameter)
<img width="965" height="193" alt="WhatsApp Image 2026-04-22 at 21 37 23" src="https://github.com/user-attachments/assets/d82e8191-702e-4668-be2e-e42690bfffe0" />
fungsi print yaitu untuk menampilkan daftar menunya 

- def main():
untuk mendefinisikan fungsi utama main()
- running = True
Membuat variabel boolean running = True untuk kontrol loop while.

- while running:
Loop while berjalan selama running bernilai True.

- menu()
memanggil fungsi menu() untuk menampilkan pilihan menu di layar.

- try:
untuk mulai kode program
<img width="1028" height="275" alt="WhatsApp Image 2026-04-22 at 21 50 17" src="https://github.com/user-attachments/assets/2ea3f5be-8e28-499e-97c6-2bc8f62a09b6" />

- if choice == 1:
jika user memilih menu pertama

- nama = input("Nama barang: ").strip()
untuk user dapat mengetikkan nama barang yang akan dimasukkan ke inventaris

- .append(nama)
untuk tambah nama barang ke akhir list inventory

- print(f"Barang '{nama}' berhasil ditambahkan.")
Print konfirmasi dengan nama barang

- else:
print("Nama barang tidak boleh kosong.")
Jika nama kosong, akan menampilkan pesan error.

<img width="979" height="435" alt="WhatsApp Image 2026-04-22 at 22 00 21" src="https://github.com/user-attachments/assets/69c7d5f4-89a7-4cf4-963b-e5d160f12287" />

- elif choice == 2
jika user memilih menu kedua

- for i, item in enumerate(inventory, 1):
agar terdapat pe-nomoran yang dimulai dari angka 1

- idx = int(input("Nomor barang yang dihapus (1-based): ")) - 1
untuk user dapat memasukkan nomor barang mana yang ingin dihapus

- if 0 <= idx < len(inventory):
untuk cek index valid (len(inventory) = panjang list)

- removed = inventory.pop(idx)
fungsi .pop(idx) untuk menghapus & return item di index idx

- print(f"Barang '{removed}' berhasil
Print barang yang dihapus

- else:
- print("Nomor tidak valid.")
- except ValueError:
- print("Masukkan nomor yang valid.")
untuk menampilkan error jika input yang dimasukkan bukan angka

<img width="984" height="297" alt="WhatsApp Image 2026-04-22 at 22 10 33" src="https://github.com/user-attachments/assets/7a9f906f-c649-49dd-9199-b375e7018bdb" />

- elif choice == 3:
jika user memilih menu ketiga

cari = input("Nama barang dicari: ").strip().lower()
agar user bisa menginputkan nama barang yang ingin dicari di inventaris

- found = False
- for i, item in enumerate(inventory):
- if cari in item.lower():
- print(f"Barang '{item}' ditemukan di posisi {i+1}.")
- found = True
- if not found:
- print("Barang tidak ditemukan.")
  pada bagian ini kita memastikan bahwa barang tersebut ada di inventaris, jika ada maka nilai found nya berubah menjadi true dan menampilkan "barang ditemukan di posisi i" dan jika tidak ditemukan akan menampilkan "barang tidak ditemukan"


<img width="1001" height="282" alt="WhatsApp Image 2026-04-22 at 22 25 55" src="https://github.com/user-attachments/assets/6b014577-402d-41ac-b941-a3189d7245df" />

- elif choice == 4:
  jika user memilih menu keempat

- print("\nList barang saat ini:", str(inventory))
  menampilkan apa saja list barang saat ini

- if inventory:
- print("Daftar barang (numbered):")
- for i, item in enumerate(inventory, 1):
- print(f"{i}. {item}")
- print(f"Total: {len(inventory)} barang")
  sistem akan menampilkan daftar barang berupa list satu dimensi dan list yang memiliki penomoran yang dimulai pada angka 1

<img width="906" height="221" alt="WhatsApp Image 2026-04-22 at 22 30 49" src="https://github.com/user-attachments/assets/749e4ddb-fb90-4b71-b702-503de97ae706" />

- elif choice == 5:
  jika user memilih menu kelima
- print("List akhir:", str(inventory))
- print("Terima kasih! Keluar dari program.")
  sistem akan menampilkan list akhir dan ucapan "Terima kasih! Keluar dari program."
-  running = False
iterasi while akan berhenti karena runningnya = false

<img width="972" height="355" alt="WhatsApp Image 2026-04-22 at 22 31 06" src="https://github.com/user-attachments/assets/d92f9a8f-4370-4d00-8e92-dc02a71d93ba" />

- else:
- print("Pilihan tidak valid. Masukkan 1-5.")
  ini akan terjadi saat user menginputkan angka selain 1-5
  
- except ValueError:
- print("Error: Masukkan angka 1-5 yang valid.")
  ini akan terjadi ketika user memasukkan input selain angka
  
- except Exception as e:
- print(f"Terjadi kesalahan: {e}")
  untuk print pesan error
  
- if __name__ == "__main__":
-  main()
  untuk memanggil fungsi main() agar program dapat dijalankan

## Penjelesan Output Kode

- output pertama
berikut adalah output yang keluar ketika user memilih menu pertama
<img width="1600" height="896" alt="WhatsApp Image 2026-04-22 at 22 42 22" src="https://github.com/user-attachments/assets/3ee28cb3-74d3-43a1-8eff-b8a0e1de94ee" />
pada contoh ini, saya menambahkan mie instan, detergen, dan minyak ke dalam list inventaris

- output kedua
berikut adalah output yang keluar ketika user memilih menu kedua
<img width="1091" height="462" alt="WhatsApp Image 2026-04-22 at 22 45 48" src="https://github.com/user-attachments/assets/9ae3428a-edef-4610-9940-f8056a720a9c" />
di sini saya contohkan dengan menghapus detergen pada list

- output ketiga
berikut adalah output yang keluar ketika user memilih menu ketiga
<img width="1179" height="274" alt="WhatsApp Image 2026-04-22 at 22 46 06" src="https://github.com/user-attachments/assets/f8172ce5-8dd6-4acd-a91a-aa86fd48193f" />
di sini saya contohkan dengan mencari 'minyak' pada list, sehingga ditemukan di posisi 2

- output keempat
berikut adalah output yang keluar ketika user memilih menu keempat
<img width="1162" height="325" alt="WhatsApp Image 2026-04-22 at 22 46 28" src="https://github.com/user-attachments/assets/29736d7f-ccaf-4a48-8537-c0f93a1e519f" />
jika memilih menu keempat, maka outputnya akan menampilkan list barang dalam list satu dimensi dan list berupa pe-nomeran, di sini list yang tersisa yaitu hanya ['mie unstan', 'minyak'] saja karena detergen sudah dihapus

- output kelima
berikut adalah output yang keluar ketika user memilih menu kelima
<img width="1026" height="331" alt="WhatsApp Image 2026-04-22 at 22 46 44" src="https://github.com/user-attachments/assets/8f38dd9a-a97f-4920-978a-f31de7549b36" />
sistem akan menampilkan list akhir dan teks 'Terima kasih! keluar dari program"

## Video Penjelasan Kode Program
- https://youtu.be/JXt07A-xakU
