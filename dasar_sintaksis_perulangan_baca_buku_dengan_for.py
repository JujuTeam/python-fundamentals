"""
Program perulangan baca buku
"""

jumlah_buku = 10
print('Ibu berkata, "Baca semua bukumu"')

jumlah_buku_dibaca = 0
print(f'Jumlah buku yang sudah dibaca {jumlah_buku_dibaca}')

for jumlah_buku_dibaca in range(1, 10+1):
    print(f"Buku ke {jumlah_buku_dibaca} sudah dibaca")

print(f"Jumlah buku yang sudah dibaca sekarang {jumlah_buku_dibaca}")