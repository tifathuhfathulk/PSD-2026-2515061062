class Node:
    def __init__(self, key, nama_barang, jumlah):
        self.key = key
        self.nama_barang = nama_barang
        self.jumlah = jumlah
        self.left = None
        self.right = None


class BSTLanjut:
    def __init__(self):
        self.root = None

    def insert_node(self, root, key, nama_barang, jumlah):
        if root is None:
            return Node(key, nama_barang, jumlah)

        if key < root.key:
            root.left = self.insert_node(root.left, key, nama_barang, jumlah)
        elif key > root.key:
            root.right = self.insert_node(root.right, key, nama_barang, jumlah)
        else:
            root.nama_barang = nama_barang
            root.jumlah = jumlah
        return root

    def insert(self, key, nama_barang, jumlah):
        self.root = self.insert_node(self.root, key, nama_barang, jumlah)

    def find_min_node(self, root):
        current = root
        while current is not None and current.left is not None:
            current = current.left
        return current

    def delete_node(self, root, key):
        if root is None:
            return None

        if key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                successor = self.find_min_node(root.right)
                root.key = successor.key
                root.nama_barang = successor.nama_barang
                root.jumlah = successor.jumlah
                root.right = self.delete_node(root.right, successor.key)

        return root

    def delete(self, key):
        self.root = self.delete_node(self.root, key)

    def search_node(self, root, key):
        if root is None:
            return None
        if root.key == key:
            return root
        if key < root.key:
            return self.search_node(root.left, key)
        return self.search_node(root.right, key)

    def search(self, key):
        return self.search_node(self.root, key)

    def sum_barang(self, root):
        if root is None:
            return 0
        return root.jumlah + self.sum_barang(root.left) + self.sum_barang(root.right)

    def find_successor(self, root, key):
        current = root
        successor = None

        while current is not None:
            if key < current.key:
                successor = current
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                break

        if current is None:
            return None, False

        if current.right is not None:
            successor = self.find_min_node(current.right)

        if successor is None:
            return None, False

        return successor.key, True

    def find_predecessor(self, root, key):
        current = root
        predecessor = None

        while current is not None:
            if key > current.key:
                predecessor = current
                current = current.right
            elif key < current.key:
                current = current.left
            else:
                break

        if current is None:
            return None, False

        if current.left is not None:
            temp = current.left
            while temp.right is not None:
                temp = temp.right
            predecessor = temp

        if predecessor is None:
            return None, False

        return predecessor.key, True

    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(f"ID: {root.key}, Nama: {root.nama_barang}, Jumlah: {root.jumlah}")
            self.inorder(root.right)


def main():
    bst = BSTLanjut()
    pilih = 0

    while pilih != 7:
        print("\n=== Sistem Inventory Barang ===")
        print("1. Tambah barang")
        print("2. Hapus barang")
        print("3. Cari barang")
        print("4. Tampilkan barang sebelumnya")
        print("5. Tampilkan barang setelahnya")
        print("6. Tampilkan jumlah seluruh barang")
        print("7. Keluar")

        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            try:
                key = int(input("Masukkan ID barang: "))
                nama = input("Masukkan nama barang: ")
                jumlah = int(input("Masukkan jumlah barang: "))
                bst.insert(key, nama, jumlah)
                print("Barang berhasil ditambahkan.")
            except ValueError:
                print("Input tidak valid!")

        elif pilih == 2:
            try:
                key = int(input("Masukkan ID barang yang akan dihapus: "))
                data = bst.search(key)
                if data is None:
                    print("Barang tidak ditemukan.")
                else:
                    bst.delete(key)
                    print("Barang berhasil dihapus.")
            except ValueError:
                print("Input tidak valid!")

        elif pilih == 3:
            try:
                key = int(input("Masukkan ID barang yang dicari: "))
                data = bst.search(key)
                if data is None:
                    print("Barang tidak ditemukan.")
                else:
                    print(f"Barang ditemukan: ID={data.key}, Nama={data.nama_barang}, Jumlah={data.jumlah}")
            except ValueError:
                print("Input tidak valid!")

        elif pilih == 4:
            try:
                key = int(input("Masukkan ID barang: "))
                ans, found = bst.find_predecessor(bst.root, key)
                if found:
                    data = bst.search(ans)
                    print(f"Barang sebelumnya: ID={data.key}, Nama={data.nama_barang}, Jumlah={data.jumlah}")
                else:
                    print("Tidak ada barang sebelumnya.")
            except ValueError:
                print("Input tidak valid!")

        elif pilih == 5:
            try:
                key = int(input("Masukkan ID barang: "))
                ans, found = bst.find_successor(bst.root, key)
                if found:
                    data = bst.search(ans)
                    print(f"Barang setelahnya: ID={data.key}, Nama={data.nama_barang}, Jumlah={data.jumlah}")
                else:
                    print("Tidak ada barang setelahnya.")
            except ValueError:
                print("Input tidak valid!")

        elif pilih == 6:
            print(f"Jumlah seluruh barang: {bst.sum_barang(bst.root)}")

        elif pilih == 7:
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()