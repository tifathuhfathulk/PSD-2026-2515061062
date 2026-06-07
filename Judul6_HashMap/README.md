# Sistem Pencarian Menu Restaurant

## Deskripsi Singkat
Sistem pencarian menu restoran adalah sistem yang memungkinkan pelanggan atau kasir untuk cepat menemukan nama menu berdasarkan kode menu yang unik. Penggunakan HashMap sangat efisien karena sistem ini bisa mencari menu dalam waktu sangat cepat (O(1)) tanpa perlu memeriksa semua menu satu per satu. HashMap menghitung langsung slot mana yang menyimpan kode menu tertentu melalui fungsi hash, sehingga meskipun restoran punya ratusan menu, pencarian tetap cepat dan tidak lambat, berbeda dengan mencari di list biasa yang harus cek satu-satu dari awal sampai akhir.

## Source Code
<img width="1920" height="1008" alt="image" src="https://github.com/user-attachments/assets/612dfdb5-2b98-43b0-92d6-32df93acc235" />
<img width="1920" height="1008" alt="image" src="https://github.com/user-attachments/assets/fc20f741-4178-4019-8747-9f721520bd8e" />
<img width="1920" height="1008" alt="image" src="https://github.com/user-attachments/assets/ef11ef0e-456f-4384-b495-3b9c4d872f0d" />

## Penjelasan Kode
- class Node: Merupakan blueprint (template) yang digunakan saat membuat Node
- def __ init__(self, key, value): merupakan fungsi yang otomatis jalan saat node pertama dibuat.
- self.key = key untuk menyimpan key
- self.value = value untuk menyimpan value.
- self.next = None penunjuk next nya masih none
- class HashMapSeparateChaining: sebagai Blueprint untuk membuat "hash table"
- def __init__(self, size=10): Fungsi otomatis saat hash table dibuat. dengan size=10 = ukuran tabel = 10 slot
- self.SIZE = size Simpan ukuran tabel (10) agar bisa dipakai nanti.
- self.table = [None] * self.SIZE Buat tabel kosong dengan 10 slot, semua masih None (kosong)
- def hash_function(self, key): mendefinisikan fusngsi hash function
- return (key % self.SIZE + self.SIZE) % self.SIZE rumus untuk menentukan indeks dalam tabel
- def insert(self, key, value): mendefinisikan fungsi untuk tambah data
- index = self.hash_function(key) menentukan indeks dengan memanggil fungsi hash function
- current = self.table[index] current merupakan node pertama di slot tersebut
- while current is not None: perulangan selama currentnya tidak None
- if current.key == key: Jika key sudah ada
- current.value = value update valuenya
- return
- current = current.next jika key tidak ada sebelumnya, pindah ke node berikutnya
- new_node = Node(key, value) Buat node baru karena key belum ada.
- new_node.next = self.table[index] Hubungkan node baru ke node yang sudah ada di slot ini.
- self.table[index] = new_node Slot ini sekarang diisi node baru (jadi node pertama)
- def search(self, key): mendefinisikan fungsi untuk mencari data berdasaekan key
- index = self.hash_function(key) hitung indeks berdasarkan key dengan memanggil fungsi hash function
- current = self.table[index] Ambil node pertama di slot tersebut.
- while current is not None: perulangan jika currentnya tidak None
- if current.key == key: jika key nya ketemu maka
- return current Return node yang ditemukan (berisi key + value).
- current = current.next jika belum ketemu maka pindah ke node berikutnya
- return None jika sudah habis semua node dan tidak ditemukan, maka return None
- def display(self): mendefinisikan fungsi untuk menampikan seluruh isi hash table
- print("\nIsi Menu Restaurant:") untuk cetak judul "Isi Menu Restaurant" di baris baru.
- for i in range(self.SIZE): Loop 10 kali (dari slot 0 sampai 9)
- print(f"{i}: ", end="") Untuk cetak nomor slot, contoh: 0: , 1: , dst.
- current = self.table[i] Ambil node pertama di slot i
- while current is not None: Loop cek semua node di slot ini
- print(f"({current.key},{current.value}) -> ", end="") Cetak key dan value, contoh: (121,Nasi Goreng Seafood) ->
- current = current.next untuk pindah ke node berikutnya.
- print("NULL") Setelah habis semua node di slot, cetak NULL (= akhir rantai)
- def main(): mendefinisikan fungsi utama, yaitu main
- hashmap = HashMapSeparateChaining() Buat objek hash table baru sesuai blueprint. Sekarang punya 10 slot kosong.
- hashmap.insert(121, "Nasi Goreng Seafood")
- hashmap.insert(144, "Mie Bangladesh")
- hashmap.insert(158, "Nasi Ayam Kecap")
- hashmap.insert(171, "Es Campur")
- hashmap.insert(136, "Jus Buah")
- hashmap.insert(188, "Teh Telor") untuk menambahkan menu berdasarkan key dan value
- hashmap.display() untuk menampilkan seluruh isi menu
- Kode_menu = int(input("Masukkan Kode Menu: ")) untuk meminta user menginputkan kode menu berupa angka
- hasil = hashmap.search(Kode_menu) mencari hasil dengan memanggil fungsi search
- if hasil is not None: jika menu ditemukan
- print(f"\nMenu dengan Kode {Kode_menu} adalah {hasil.value}") Cetak nama menu yang ditemukan. Contoh: Menu dengan Kode 121 adalah Nasi Goreng Seafood.
- else: jika hasil None
- print(f"\nMenu dengan kode {Kode_menu} tidak ditemukan") Cetak pesan tidak ditemukan.
- if __name__ == "__main__": Cek: apakah file ini jalan sebagai program utama? (bukan di-import sebagai modul).
- main() Jika ya, jalankan fungsi main().
  
## Penjelasan Output
<img width="1920" height="1008" alt="image" src="https://github.com/user-attachments/assets/97bf56d4-339d-489d-9bad-4d2207510733" />

- Ketika program dijalankan, maka outputnya akan langsung menampilkan isi dari hash map karena kita memanggil fungsi display.
- Kemudian User diminta memasukkan kode menu yang ingin mereka cari dalam bentuk angka
- Kemudian sistem akan menampilkan hasil pencarian dengan mencetak hasil seperti "Menu dengan Kode 121 adalah Nasi Goreng Seafood." atau jika tidak ditemukan maka akan menampilkan "Menu dengan kode {Kode_menu} tidak ditemukan"
  
## Link YouTube
- https://youtu.be/kPMZUFTYkT0
