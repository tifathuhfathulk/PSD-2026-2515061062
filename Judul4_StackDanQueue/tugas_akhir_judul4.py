class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class QueueLinkedList:
    def __init__(self):
        self.front_ptr = None
        self.rear_ptr = None
 
    def is_empty(self):
        return self.front_ptr is None
 
    def enqueue(self, x):
        new_node = Node(x)
        if self.is_empty():
            self.front_ptr = new_node
            self.rear_ptr = new_node
        else:
            self.rear_ptr.next = new_node
            self.rear_ptr = new_node
        print(f"Pelanggan {x} berhasil ditambahkan")
 
    def dequeue(self):
        if self.is_empty():
            print("Antrian kosong")
            return
        temp = self.front_ptr
        print(f"Antrian {temp.data} berhasil dihapus")
        self.front_ptr = self.front_ptr.next
        if self.front_ptr is None:
            self.rear_ptr = None
 
    def peek(self):
        if self.is_empty():
            print("Antrian kosong")
            return
        print(f"Antrian terdepan, yaitu atas nama : {self.front_ptr.data}")
    
    def display(self):
        if self.is_empty():
            print("Antrian kosong")
            return
        print("Seluruh Antirian Saat ini: ", end="")
        current = self.front_ptr
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print() 

def main():
    queue = QueueLinkedList()
    pilih = 0
    while pilih != 5:
        print("\n=== Waiting List Restaurant ===")
        print("1. Menambahkan Antrian")
        print("2. Menghapus Antrian")
        print("3. Melihat Antrian Terdepan")
        print("4. Melihat Seluruh Data Antrian")
        print("5. Keluar Pogram")
        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue
        if pilih == 1:
            try:
                val = str(input("Masukkan Nama Pelanggan: "))
                queue.enqueue(val)
            except ValueError:
                print("Input tidak valid!")
        elif pilih == 2:
            queue.dequeue()
        elif pilih == 3:
            queue.peek()
        elif pilih == 4:
            queue.display()
        elif pilih == 5:
            while not queue.is_empty():
                queue.dequeue()
            print("Program selesai.")
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
