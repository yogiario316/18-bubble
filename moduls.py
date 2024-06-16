nama = ["Nama: Yogi Ario Pratama", "NPM: 2313020004", "Kelas: 1J", "Materi: Binnary Search"]
for i in nama:
    print(i)
print("\n")

def mhitung():
    for f,k in enumerate(ar):
        if k == find:
            return f"Ditemukan pada index {f}"
        break
    return "tidak ditemukan"
ar = [1, 5, 9, 33, 98, 1000, 657, 222, 765, 90, 9999, 76, 90]
print(ar)
find = int(input("Masukkan angka: "))

hasil = mhitung()
print(hasil)