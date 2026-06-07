class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMapSeparateChaining:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [None] * self.SIZE

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next
        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                return current
            current = current.next
        return None

    def display(self):
        print("\nIsi Menu Restaurant:")
        for i in range(self.SIZE):
            print(f"{i}: ", end="")
            current = self.table[i]
            while current is not None:
                print(f"({current.key},{current.value}) -> ", end="")
                current = current.next
            print("NULL")

def main():
    hashmap = HashMapSeparateChaining()
    hashmap.insert(121, "Nasi Goreng Seafood")
    hashmap.insert(144, "Mie Bangladesh")
    hashmap.insert(158, "Nasi Ayam Kecap")
    hashmap.insert(171, "Es Campur")
    hashmap.insert(136, "Jus Buah")
    hashmap.insert(188, "Teh Telor")
    hashmap.display()

    Kode_menu = int(input("Masukkan Kode Menu: "))
    hasil = hashmap.search(Kode_menu)
    if hasil is not None:
        print(f"\nMenu dengan Kode {Kode_menu} adalah {hasil.value}")
    else:
        print(f"\nMenu dengan kode {Kode_menu} tidak ditemukan")

    hashmap.display()

if __name__ == "__main__":
    main() 