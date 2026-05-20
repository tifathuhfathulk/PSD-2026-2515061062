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
-  return root.left  maka anak kiri naik menggantikan posisi node ini.
- else: jika node punya dua anak
-  successor = self.find_min_node(root.right) cari nilai terkecil dari nilai yang lebih besar dulu
-  root.key = successor.key isi data node yang dihapus dengan data successor
-  root.jumlah = successor.jumlah
-  root.right = self.delete_node(root.right, successor.key) lalu hapus successor yang lama
-   return root mengembalikan hasil pohon setelah penghapusan selesai.
-   def delete(self, key): fungsi ini pemanggilan utama untuk hapus barang berdasarkan ID.
- self.root = self.delete_node(self.root, key) Hasilnya disimpan kembali ke self.root.
- def search_node(self, root, key): mendefinisikan fungsi untuk mencari barangberdasarkan ID barangnya.
- 
## Penjelasan Output
## Link YouTube
