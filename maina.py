nama =  "Nama: Yogi Ario Pratama", "NPM: 2313020004", "Kelas: 1J", "Materi: Binnary Search" 
for i in nama:
    print(i)
print("\n")

def mhitung(ar, find):
    f=0
    k=len(ar)-1
    mid=int((f+k)/2)
    hasil="Tidak ditemukan"

    while (f<=k):
        if  ar[mid]  == find:
            hasil=f"Ditemukan pada index {mid}"
            break
        elif  ar[mid]  > find:
            k = mid-1
            mid = int((f+k)/2)
        elif  ar[mid]  < find:
            f = mid+1
            mid = int((f+k)/2)

    return hasil
def result():
    pass