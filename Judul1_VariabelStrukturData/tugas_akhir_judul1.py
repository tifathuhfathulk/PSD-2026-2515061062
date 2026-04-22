# Membuat Program List Inventaris Barang di Toko

inventory = []  # List untuk menyimpan nama barang

def menu():
    print("\n---- DAFTAR INVENTARIS BARANG TOKO -----")
    print("1. Tambahkan barang")
    print("2. Hapus barang")
    print("3. Cek barang dalam list")
    print("4. Tampilkan semua barang")
    print("5. Keluar")

def main():
    running = True
    while running:
        menu()
        try:
            choice = int(input("Pilih menu (1-5): "))
            
            if choice == 1:
                nama = input("Nama barang: ").strip()
                if nama:
                    inventory.append(nama)
                    print(f"Barang '{nama}' berhasil ditambahkan.")
                else:
                    print("Nama barang tidak boleh kosong.")
                    
            elif choice == 2:
                if inventory:
                    print("\nDaftar barang:")
                    for i, item in enumerate(inventory, 1):
                        print(f"{i}. {item}")
                    try:
                        idx = int(input("Nomor barang yang dihapus (1-based): ")) - 1
                        if 0 <= idx < len(inventory):
                            removed = inventory.pop(idx)
                            print(f"Barang '{removed}' berhasil dihapus.")
                        else:
                            print("Nomor tidak valid.")
                    except ValueError:
                        print("Masukkan nomor yang valid.")
                else:
                    print("Inventory kosong, tidak ada barang untuk dihapus.")
                    
            elif choice == 3:
                cari = input("Nama barang dicari: ").strip().lower()
                found = False
                for i, item in enumerate(inventory):
                    if cari in item.lower():
                        print(f"Barang '{item}' ditemukan di posisi {i+1}.")
                        found = True
                if not found:
                    print("Barang tidak ditemukan.")
                    
            elif choice == 4:
                print("\nList barang saat ini:", str(inventory))
                if inventory:
                    print("Daftar barang (numbered):")
                    for i, item in enumerate(inventory, 1):
                        print(f"{i}. {item}")
                    print(f"Total: {len(inventory)} barang")
                else:
                    print("Inventory kosong.")
                    
            elif choice == 5:
                print("List akhir:", str(inventory))
                print("Terima kasih! Keluar dari program.")
                running = False
                
            else:
                print("Pilihan tidak valid. Masukkan 1-5.")
                
        except ValueError:
            print("Error: Masukkan angka 1-5 yang valid.")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    main()
