def sequential_search(data, n, target):
    
    i = 0
    counter = 0
    while i < n:
        if data[i] == target:
            counter += 1
        i += 1
    return counter

def main():
    
    suara_pemilih = [
        1,2,1,2,3,1,2,2,1,3, 2,3,3,3,1,2,3,1,2,1,
        2,3,1,2,1,3,2,1,2,3, 1,2,3,1,2,1,3,2,1,2,
        3,1,1,1,3,3,1,2,3,1, 2,1,3,3,1,2,3,1,2,1,
        3,2,1,2,3,1,2,1,3,2, 1,3,2,1,2,3,1,2,1,3,
        2,1,3,2,1,2,3,1,2,1
    ]
    
    n = len(suara_pemilih)
    print("=== SISTEM PERHITUNGAN SUARA PILKADA ===")
    print("Paslon 1: Naruto-Sasuke")
    print("Paslon 2: Nagi-Reo") 
    print("Paslon 3: Martin-James")
    print(f"\nData suara {n} pemilih: {suara_pemilih[:10]}...") 
    
    # Untuk menghitung seluruh suara
    suara = [0, 0, 0, 0]
    print("\n--- HASIL PERHITUNGAN ---")
    print("Paslon\tSuara\tPersentase")
    print("-"*25)
    
    total_suara = 0
    for paslon in [1, 2, 3]:
        counter = sequential_search(suara_pemilih, n, paslon)
        suara[paslon] = counter
        total_suara += counter
        persen = (counter/n)*100
        print(f"{paslon}\t{counter}\t{persen:.1f}%")
    
    paslon_nama = {1: "Naruto-Sasuke", 2: "Nagi-Reo", 3: "Martin-James"}
    pemenang = max(range(1,4), key=lambda x: suara[x])
    suara_pemenang = suara[pemenang]
    
    print(f"\nTotal suara: {total_suara}/{n}")
    print(f"Paslon Pemenang {pemenang}: {paslon_nama[pemenang]}")
    print(f"Suara: {suara_pemenang} ({(suara_pemenang/n)*100:.1f}%)")

if __name__ == "__main__":
    main()