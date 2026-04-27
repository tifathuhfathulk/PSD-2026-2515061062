def tukar(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def bubble_sort_desc(arr, n):
    # Mengurutkan dari terbesar ke terkecil untuk high score
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] < arr[j + 1]:   
                tukar(arr, j, j + 1)


def main():
    try:
        n = int(input("Masukkan jumlah pemain: "))
        if n <= 0:
            print("Jumlah pemain harus lebih dari 0!")
            return
    except ValueError:
        print("Input tidak valid!")
        return

    skor = []
    nama = []

    print("Masukkan data pemain (nama skor):")
    for i in range(n):
        while True:
            try:
                data = input().strip().split()
                if len(data) != 2:
                    print("Format: nama skor (contoh: Ali 1500)")
                    continue
                nama_pemain = data[0]
                nilai_skor = int(data[1])
                nama.append(nama_pemain)
                skor.append(nilai_skor)
                break
            except ValueError:
                print("Skor harus berupa angka!")

    print("\nSkor sebelum diurutkan:")
    for i in range(n):
        print(f"{i+1}. {nama[i]} | Skor: {skor[i]}")

    bubble_sort_desc(skor, n)

    print("\nRanking skor tertinggi (High Score):")
    for i in range(n):
        print(f"{i+1}. Skor: {skor[i]}")


if __name__ == "__main__":
    main()
