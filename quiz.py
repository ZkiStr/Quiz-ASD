###SOAL NO 1
###Membuat pengecekan username yang diawali @ diikuti alphabet dan angka,
###Tidak wajib diakhiri _
###output = PASS / FAILED
import re
us= '@Zaki229_'
pola = r'@[a-zA-Z_]+[0-9.\_]+'
cek = re.findall(pola, us)
if cek:
    if us== cek[0]:
        print('PASS')
    elif us!= cek[0]:
        print('FAILED')
else:
    print('FAILED')

###SOAL NO 2
###Mencari email di sebuah teks atau paragraf
open_file = open('text.txt', 'r', encoding='latin1')
w = open_file.read()
open_file.close()
pola = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
hasil = re.findall(pola, w)
print(hasil)

###SOAL NO 3
###Mencari daun simpul luar
class _SimpulPohonBiner(object):
    def __init__(self, data):
        self.data = data
        self.kiri = None
        self.kanan = None

    

#Membuat simpul-simpul dan mengisi data
A = _SimpulPohonBiner('43')
B = _SimpulPohonBiner('10')
C = _SimpulPohonBiner('79')
D = _SimpulPohonBiner('9')
E = _SimpulPohonBiner('12')
F = _SimpulPohonBiner('54')
G = _SimpulPohonBiner('90')
H = _SimpulPohonBiner('11')


# Menghubungkan simpul ortu-anak
A.kiri = B; A.kanan = C
B.kiri = D; B.kanan = E
C.kiri = F; C.kanan = G
E.kiri = H

def subkiri(subpohon):
    if subpohon is not None:
        subkiri(subpohon.kanan)
        print(subpohon.data)
        
        

def subkanan(subpohon):
    if subpohon is not None:
        print(subpohon.data)
        subkanan(subpohon.kiri)
            
subkanan(A)
subkiri(A)
