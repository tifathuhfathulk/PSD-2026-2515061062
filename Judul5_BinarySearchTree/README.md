# Program Inventory Barang

## Deskripsi Singkat
Program inventory barang ini dibuat untuk memudahkan pengelolaan data barang secara sederhana, seperti menambah, menghapus, mencari, serta menampilkan barang sebelumnya dan sesudahnya berdasarkan ID. Tujuan utamanya adalah agar proses pengelolaan stok menjadi lebih cepat, rapi, dan teratur tanpa harus memeriksa data secara manual satu per satu. Struktur BST digunakan sebagai dasar penyimpanan data karena BST menyusun barang berdasarkan urutan ID, sehingga proses pencarian, penambahan, dan penghapusan dapat dilakukan lebih efisien. Dengan BST, data barang juga bisa ditelusuri secara terurut dari ID terkecil hingga terbesar.
## Source Code
<img width="1920" height="1008" alt="TA5_1" src="https://github.com/user-attachments/assets/66ed2c57-0ead-4333-9597-39422fb87a77" />
<img width="1920" height="1008" alt="TA5_2" src="https://github.com/user-attachments/assets/3b189b8f-15ac-434a-a54a-2f7227de08c8" />
<img width="1920" height="1008" alt="TA5_3" src="https://github.com/user-attachments/assets/3a81d6fd-904e-42f7-86c3-6e3d595217a4" />
<img width="1920" height="1008" alt="TA5_4" src="https://github.com/user-attachments/assets/8ac467c3-d0ca-406a-93d7-0308ca9bd46c" />
<img width="1920" height="1008" alt="TA5_5" src="https://github.com/user-attachments/assets/eb480ab4-87eb-41d8-bb38-7d73ca05eb17" />
<img width="1920" height="1008" alt="TA5_6" src="https://github.com/user-attachments/assets/1a5f6fa5-f845-4676-8b92-b53e8236a297" />
<img width="1920" height="1008" alt="TA5_7" src="https://github.com/user-attachments/assets/942fd70f-4da0-47eb-8f06-de1b7f032be6" />
<img width="1920" height="1008" alt="TA5_8" src="https://github.com/user-attachments/assets/7fdfa1cd-a79a-444f-ac1c-08b25d8f0738" />

## Penjelasan Kode
- class Node: Ini adalah cetakan atau blueprint untuk membuat satu node.
- def __ init__(self, key, nama_barang, jumlah): Ini adalah fungsi khusus yang otomatis dijalankan saat node baru dibuat.
Isinya adalah data awal yang ingin dimasukkan.
- self.key = key di sini key nya adalah ID barang
- self.nama_barang = nama_barang variabel untuk menyimpan nama barang
- self.jumlah = jumlah variabel untuk menyimpan jumlah barang.
- self.left = None bagian kiri node nya masih kosong
- self.right = None bagian kanan nodenya juga masih kosong.
- class BSTLanjut: Ini adalah cetakan untuk membuat pohon BST
- def __ init__(self): merupakan fungsi awal saat BST dibuat
- self.root = None awalnya rootnya masih kosong
- def insert_node(self, root, key, nama_barang, jumlah): fungsi untuk menambahkan barang ke dalam inventory atau menambah node ke pohon
- if root is None: mengecek jika rootnya kosong
- return Node(key, nama_barang, jumlah) maka buat node baru yang berisi id, nama barang, dan jumalah barang.
- if key < root.key: untuk mengecek apakah key lebih kecil daripada root nya
- root.left = self.insert_node(root.left, key, nama_barang, jumlah) jika iya maka masukkan key nya ke sebelah kiri root
- elif key > root.key: mengecek apakah key-nya lebih besar daripada root
- root.right = self.insert_node(root.right, key, nama_barang, jumlah) jika iya maka masukkan key nya ke sebelah kanan root
- else: selain itu
- root.nama_barang = nama_barang
- root.jumlah = jumlah kalau key sama berarti ID nya sudah ada maka data lama akan di update
- return root untuk mengembalikan node root yang sudah diperbarui.
- def insert(self, key, nama_barang, jumlah): untuk mendefinisikan fungsi insert sederhana yang akan memanggil fungsi insert di atasnya tadi
- self.root = self.insert_node(self.root, key, nama_barang, jumlah) memangil fungsi insert sebelumnya dan akan brulang
- def find_min_node(self, root): mendefinisikan fungsi min untuk mencari ID barang yang paling kecil
- current = root artinya mulai dari node awal
- while current is not None and current.left is not None: artinya selama masih ada node di kiri, terus bergerak ke kiri.
- current = current.left geser terus ke kiri sampai nilai paling bawah/akhir
- return current mengembalikan nilai terkecil
- def delete_node(self, root, key): untuk mendefinisikan fungsi hapus barang
- if root is None: untuk mengecek jika root nya masih kosong
- return None kalau masih kosong berarti tidak ada yang bisa diahapus
-if key < root.key: jika key nya lebih kecil daripada root
- root.left = self.delete_node(root.left, key) maka cari di sebelah kiri
- elif key > root.key: atau jika key nya lebih besar dari root
- root.right = self.delete_node(root.right, key) cari di sbelah kiri
- else: kalau sudah ketemu node yang mau dihapus
- if root.left is None and root.right is None: jika root kira dan kanannya kosong
- return None berarti bisa langsung dihapus
- elif root.left is None: jika root kirinya kosong
- return root.right maka anak kanan naik menggantikan posisi node ini.
- elif root.right is None: atau jika root kanannya kosong
- return root.left  maka anak kiri naik menggantikan posisi node ini.
- else: jika node punya dua anak
- successor = self.find_min_node(root.right) cari nilai terkecil dari nilai yang lebih besar dulu
- root.key = successor.key isi data node yang dihapus dengan data successor
- root.jumlah = successor.jumlah
- root.right = self.delete_node(root.right, successor.key) lalu hapus successor yang lama
- return root mengembalikan hasil pohon setelah penghapusan selesai.
- def delete(self, key): fungsi ini pemanggilan utama untuk hapus barang berdasarkan ID.
- self.root = self.delete_node(self.root, key) Hasilnya disimpan kembali ke self.root.
- def search_node(self, root, key): mendefinisikan fungsi untuk mencari barangberdasarkan ID barangnya.
- if root is None: jika rootnya kosong
- return None berartiberarti hasilnya tidak ada
- if root.key == key: jika root = key berarti ketemu
- return root kembalikan node tersebut
- if key < root.key: jika key lebih kecil daripada root,
- return self.search_node(root.left, key) maka cari di sebelah kiri
- return self.search_node(root.right, key) jika tidak cari di sebelah kanan
- def search(self, key):
- return self.search_node(self.root, key) mendefinisikan fungsi search sederhana yang memanggil fungsi yang diatasnya tadi
- def sum_barang(self, root): mendefinisikan fungsi untuk mengitung total stok barang
- if root is None: jika rootnya masih kosong.
- return 0 maka akan mengembalikan nilai 0
- return root.jumlah + self.sum_barang(root.left) + self.sum_barang(root.right) jika tidak maka ambil juamlah node sekarang, tambahkan jumlah dari kiri dan tambahkan juamlah dari kanan
- def find_successor(self, root, key): mendefinisikan fungsi untuk mencari nilai terkecil dari nilai yang lebih besar (mencari nilai barang setelahnya)
- current = root current dipakai untuk menelusuri pohon.
- successor = None successor menyimpan calon barang setelah ID yang dicari.
- while current is not None: melakukan perulangan selama current tidak kosong
- if key < current.key: jika key lebih kecil dari node sekarang:
- successor = current
- current = current.left lanjut ke bagian kiri
- elif key > current.key: jika key lebih besar
- current = current.right maka lanjut ke sebelah kanan
- else:
- break berhenti karena barang yang dicari sudah ditemukan
- if current is None: jika barangnya tidak sitemukan
- return None, False kembalikan hasil gagal
- if current.right is not None: Kalau node yang dicari punya anak kanan
- successor = self.find_min_node(current.right) successor sebenarnya adalah node paling kecil di kanan.
- if successor is None: Kalau tidak ada successor
- return None, False berarti memang tidak punya barang setelahnya.
- return successor.key, True Mengembalikan ID successor dan tanda bahwa sukses
- def find_predecessor(self, root, key): mendifinisikan fungsi untuk mencari nilai terbesar dari yang lebih kecil (mencarinilai barang sebelumnya)
- current = root current dipakai untuk menelusuri pohon.
- predecessor = None
- while current is not None: perulangan selama current tidak kosong
-  if key > current.key:
-  predecessor = current
-  current = current.right
  jika key lebih besar diabandingkan current maka bisa jadi predecsessor lalu cari ke kanan
- elif key < current.key: atau jika key lebih kecil daripada current maka
- current = current.left cari ke bagian kiri
- else:
- break kalau nilainya sama maka berhenti
- if current is None:
- return None, False jika barang tidak ditemukan, gagal.
- if current.left is not None:
- temp = current.left kalau node yang dicari punya anak kiri, predecessor adalah node paling besar di subtree kiri.
- while temp.right is not None:
- temp = temp.right mulai dari anak kiri, lalu terus ke kanan sampai node paling akhir
- if predecessor is None: jika tidak ada predecsessor
- return None, False maka kembalikan nilai false
- return predecessor.key, True Mengembalikan ID predecessor dan tanda sukses.
- def main(): mendefinisikan fungsi main() sebagai fungsi utamanya
- bst = BSTLanjut() untuk membuat pohon inventory.
- pilih = 0 dipakai untuk menyimpan pilihan menu.
- while pilih != 7: Program akan terus berjalan sampai user memilih menu 7.
- print("\n=== Sistem Inventory Barang ===")]
- print("1. Tambah barang")
- print("2. Hapus barang")
- print("3. Cari barang")
- print("4. Tampilkan barang sebelumnya")
- print("5. Tampilkan barang setelahnya")
- print("6. Tampilkan jumlah seluruh barang")
- print("7. Keluar") Menampilkan pilihan menu yang bisa dipakai user.
- try: menjalankan kode
- pilih = int(input("Pilih: ")) mendefinisikan variabel pilih untuk user memilih menunya
- except ValueError:
- print("Input tidak valid!") Kalau input bukan angka, muncul pesan error.
- continue membuat program kembali ke awal loop. 
- if pilih == 1: jika user memilih menu 1
- key = int(input("Masukkan ID barang: "))
- nama = input("Masukkan nama barang: ")
- jumlah = int(input("Masukkan jumlah barang: ")) user memasukkan ID, nama, dan jumlah barang.
- bst.insert(key, nama, jumlah) lalu simpan ke BST
- print("Barang berhasil ditambahkan.") setelah itu tampilkan pesan berhasil
- elif pilih == 2: jika user memilih menu kedua
- key = int(input("Masukkan ID barang yang akan dihapus: ")) User memasukkan ID barang.
- data = bst.search(key) Program cek dulu apakah barang ada.
- if data is None: kalau data tidak ada
- print("B.") akan menampilkan pesan barang tidak ditemukan
- else:
- bst.delete(key) kalau ditemukan, baru dihapus.
- print("Barang berhasil dihapus.") menampilkan pesan barang erhasil dihapus
- elif pilih == 3: jika user memilih menu 3
- key = int(input("Masukkan ID barang yang dicari: ")) user diminta memasykkan ID barang yang iingin dicari
- data = bst.search(key) program cek dulu apakah barang ada.
- if data is None: Jika data barang tidak ada
- print("Barang tidak ditemukan.") maka menampilkan pesan barang tidak ditemukan
- else:
- print(f"Barang ditemukan: ID={data.key}, Nama={data.nama_barang}, Jumlah={data.jumlah}") jika ketemu maka akan menampilkan pesan barang ditemukan beserta data barangnya
- elif pilih == 4: jika user memilih menu 4
- key = int(input("Masukkan ID barang: ")) maka user akan diminta memasukkan ID barang terlebih dahulu
- ans, found = bst.find_predecessor(bst.root, key) kemudian program mencari predecessor dari ID tersebut.
- if found: jika data ditemukan
- data = bst.search(ans)
- print(f"Barang sebelumnya: ID={data.key}, Nama={data.nama_barang}, Jumlah={data.jumlah}") maka akan menampilkan barang sebelumnya dan data barang tersebut.
- else: kalau tudak ditemukan
- print("Tidak ada barang sebelumnya.")muncul pesan bahwa barang sebelumnya tidak ada
- elif pilih == 5: jika user memilih menu 5
- key = int(input("Masukkan ID barang: ")) program akan meminta user untuk memasukkan ID barang
- ans, found = bst.find_successor(bst.root, key) kemudian program mencari predecessor dari ID tersebut.
- if found: jika data ditemukan
- data = bst.search(ans)
- print(f"Barang setelahnya: ID={data.key}, Nama={data.nama_barang}, Jumlah={data.jumlah}") maka akan menampilkan barang setelahnya dan data barang tersebut.
- else: kalau tidak ditemukan
- print("Tidak ada barang setelahnya.")muncul pesan bahwa barang setelahnya itu tidak ada
- elif pilih == 6: jika user memilih menu 6
- print(f"Jumlah seluruh barang: {bst.sum_barang(bst.root)}") maka program akan memanggil fungsi sum dan menampilkan jumlah seluruh barang
- elif pilih == 7: jika user memilih menu 7 (keluar program)
- print("Program selesai, Terima Kasih!.") maka akan menampilkan pesan program selesai
- else:
- print("Pilihan tidak valid!") kalau user memasukkan angka selain 1–7, program memberi pesan error.
- if __ name__ == "__ main__":
- main() memanggil fungsi main untuk menjalankan programnya
  
## Penjelasan Output
<img width="1920" height="1008" alt="TA5 OUTPUT 1" src="https://github.com/user-attachments/assets/4fdf9a10-a684-4f02-8b64-4eae811765b6" />
<img width="1920" height="1008" alt="TA5 OUTPUT 2" src="https://github.com/user-attachments/assets/801146c7-6915-4bfc-a728-96a8600f72be" />
<img width="1920" height="1008" alt="TA5 OUTPUT 3" src="https://github.com/user-attachments/assets/eed6a101-ee7a-406f-b743-9e5cfa190876" />
<img width="1920" height="1008" alt="TA5 OUTPUT 4" src="https://github.com/user-attachments/assets/d33d64ee-064e-49c9-87e6-723d152ed83c" />

## Link YouTube
